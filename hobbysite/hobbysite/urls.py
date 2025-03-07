from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('wiki', include('wiki.urls', namespace="wiki")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('forum/', include('forum.urls', namespace="forum")),
    path('commissions/', include('commissions.urls', namespace="commissions")),
    path('admin/', admin.site.urls),
]
