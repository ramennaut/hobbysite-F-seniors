from django.urls import path

from . import views


urlpatterns = [
    path('articles/', views.list_view, name='list_view'),
    path('article/<int:id>/', views.detail_view, name='detail_view'),
    path('category/<int:id>/', views.category_view, name='category_view')
]

app_name = 'blog'