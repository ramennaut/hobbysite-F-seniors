from django.urls import path
from . import views

app_name = 'wiki'

urlpatterns = [
    path('articles/', views.list_view, name='article_list'),
    path('article/<int:id>/', views.detail_view, name='article_detail'),
    path('category/<int:id>/', views.category_view, name='category_list'),
]
