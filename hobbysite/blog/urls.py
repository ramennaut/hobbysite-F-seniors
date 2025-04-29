from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('articles/', views.list_view, name='list_view'),
    path('article/<int:id>/', views.detail_view, name='detail_view'),
    path('category/<int:id>/', views.category_view, name='category_view'),
    path('article/add/', views.add_article, name="add_article"),
    path('article/<int:id>/edit/', views.edit_article, name="edit_article"),
    #path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    #path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout"),
]

app_name = 'blog'