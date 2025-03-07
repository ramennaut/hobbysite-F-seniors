from django.shortcuts import render, get_object_or_404
from .models import Article, ArticleCategory

def list_view(request):
    articles = Article.objects.all()
    categories = ArticleCategory.objects.all()
    return render(request, 'wiki/article_list.html', {
        'articles': articles,
        'categories': categories,
    })

def detail_view(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'wiki/article_detail.html', {'article': article})

def category_view(request, id):
    category = get_object_or_404(ArticleCategory, id=id)
    articles = Article.objects.filter(category=category)
    return render(request, 'wiki/category_list.html', {
        'category': category,
        'articles': articles,
    })
