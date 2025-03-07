from django.contrib import admin
from django.urls import include, path
from wiki import views as wiki_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wiki/', include('wiki.urls')),
    path('', wiki_views.list_view, name='home'),  
]
