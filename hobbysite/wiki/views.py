from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ArticleCategory

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'wiki/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'wiki/article_detail.html', {'article': article})

def home(request):
    return redirect('wiki:article_list')
