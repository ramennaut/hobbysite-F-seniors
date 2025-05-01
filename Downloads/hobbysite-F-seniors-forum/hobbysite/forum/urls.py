from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.index, name='index'),
    path('threads/', views.thread_list, name='forum_threads'), # list view
    path('thread/<int:pk>/', views.thread_detail, name='forum_thread_1'), # detail view
    path('thread/add/', views.thread_create, name='forum_thread_create'), # create view
    path('thread/<int:pk>/edit/', views.thread_update, name='forum_thread_update'), # edit view
]
