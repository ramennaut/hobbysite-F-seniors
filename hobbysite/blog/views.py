from django.shortcuts import render
from .models import Article, ArticleCategory

def list_view(request):
    articles = Article.objects.all()
    categories = ArticleCategory.objects.all()
    ctx = {
        'articles': articles,
        'categories': categories,
    }
    return render(request, 'blog/article_list.html', ctx)

def detail_view(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/article_detail.html', {'article': article})

def category_view(request, id):
    category = ArticleCategory.objects.get(id=id)
    articles = Article.objects.filter(category=category)
    return render(request, 'blog/category_list.html', {'category': category, 'articles': articles})