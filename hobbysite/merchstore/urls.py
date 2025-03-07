from django.urls import path
from .views import MerchstoreDetailView, MerchstoreListView

urlpatterns = [
    path(
        'items',
        MerchstoreListView.as_view(),
        name='products'),
    path(
        'item/<int:pk>',
        MerchstoreDetailView.as_view(),
        name='product'),
]

app_name = 'Merchstore'
