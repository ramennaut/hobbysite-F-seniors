from django.urls import path
from .views import index
from .views import commissions_list
from .views import commissions_1

urlpatterns = [
    path('', index, name='index'),
    path('list/', commissions_list, name='commissions_list'),
    path('detail/1', commissions_1, name='commissions_1'),
]

app_name = 'commissions'