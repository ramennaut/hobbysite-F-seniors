from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm

class ArticleListView(ListView):
    model = Article
    template_name = 'wiki/article_list.html'
    context_object_name = 'articles'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        categories = ArticleCategory.objects.order_by('name')
        context['categories'] = categories

        all_articles = Article.objects.order_by('-created_on')
        
        if self.request.user.is_authenticated:
            user_articles = all_articles.filter(author__user=self.request.user)
            context['user_articles'] = user_articles

            all_articles = all_articles.exclude(author__user=self.request.user)
        
        categorized_articles = {}
        for category in categories:
            categorized_articles[category] = all_articles.filter(category=category)
        
        context['categorized_articles'] = categorized_articles
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/article_detail.html'
    context_object_name = 'article'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        
        if article.category:
            context['related_articles'] = Article.objects.filter(
                category=article.category
            ).exclude(id=article.id)[:2]
        
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm()
            
        context['comments'] = article.comments.all().order_by('-created_on')
        
        return context
    
    def post(self, request, *args, **kwargs):
        article = self.get_object()
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.article = article
                comment.author = request.user.profile
                comment.save()
                return redirect('wiki:article_detail', pk=article.pk)
        return self.get(request, *args, **kwargs)
    

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'wiki/article_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
    

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'wiki/article_form.html'
    
    def test_func(self):
        article = self.get_object()
        return article.author.user == self.request.user
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form