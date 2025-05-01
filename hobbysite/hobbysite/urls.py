from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from user_management.views import HomepageListView
#from wiki import views as wiki_views

urlpatterns = [
    path('', HomepageListView.as_view(), name='homepage'),
    path('admin/', admin.site.urls),
    path('homepage/', include('user_management.urls')),
    path('merchstore/', include('merchstore.urls', namespace='merchstore')), 
    path('wiki/', include('wiki.urls', namespace="wiki")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('forum/', include('forum.urls', namespace="forum")),
    path('commissions/', include('commissions.urls', namespace="commissions")),
    
]
