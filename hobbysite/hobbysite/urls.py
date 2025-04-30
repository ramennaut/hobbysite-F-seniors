from django.contrib import admin
from django.urls import include, path
from wiki import views as wiki_views

urlpatterns = [
    path('merchstore/', include('merchstore.urls', namespace='merchstore')), 
    path('wiki/', include('wiki.urls', namespace="wiki")),
    #path('', wiki_views.home, name='home'),
    path('blog/', include('blog.urls', namespace="blog")),
    path('forum/', include('forum.urls', namespace="forum")),
    path('commissions/', include('commissions.urls', namespace="commissions")),
    path('admin/', admin.site.urls),
]
