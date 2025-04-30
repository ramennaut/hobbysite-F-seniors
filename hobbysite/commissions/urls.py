from django.urls import path
from .views import commision_list, commission_detail

urlpatterns = [
    path('list/', commision_list.as_view(), name='commissions_list'),
    path('detail/<int:pk>/',commission_detail.as_view(), name='commissions_detail'),
]

app_name = 'commissions'