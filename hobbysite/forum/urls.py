from django.urls import path
from .views import index
from .views import forum_threads
from .views import forum_thread_1

urlpatterns = [
    path('', index, name='index'),
    path('threads/', forum_threads, name='forum_threads'),
    path('thread/1', forum_thread_1, name='forum_thread_1'),
]

app_name = 'commissions'