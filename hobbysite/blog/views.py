from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm

def list_view(request):
    articles = Article.objects.all()
    categories = ArticleCategory.objects.all()

    authored_articles = None
    non_authored_articles = articles

    if request.user.is_authenticated:
        authored_articles = articles.filter(author=request.user)
        non_authored_articles = articles.exclude(author=request.user)

    ctx = {
        'authored_articles': authored_articles,
        'articles': non_authored_articles,
        'categories': categories,
    }
    return render(request, 'blog/article_list.html', ctx)

def detail_view(request, id):
    article = Article.objects.get(id=id)
    comment = Comment.objects.filter(article=article).order_by('created_on')

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()

    ctx = {
        'article': article,
        'comment': comment,
    }

    return render(request, 'blog/article_detail.html', ctx)

def category_view(request, id):
    category = ArticleCategory.objects.get(id=id)
    articles = Article.objects.filter(category=category)
    return render(request, 'blog/category_list.html', {'category': category, 'articles': articles})

@login_required
def add_article(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:list')
        
    ctx = {
        "form": form,
    }

    return render(request, "blog/add_article.html", ctx)

@login_required
def edit_article(request, id):
    article = Article.objects.get(id=id)
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('blog:detail', id=article.id)

    ctx = {
        'form': form,
        'article': article,
    } 

    return render(request, "blog/add_article.html", ctx)