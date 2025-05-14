from django.urls import path
from .views import (
    CartListView,
    MerchstoreDetailView,
    MerchstoreListView,
    ProductCreateView,
    ProductUpdateView,
    TransactionListView
)

urlpatterns = [
    path(
        'items',
        MerchstoreListView.as_view(),
        name='products'),
    path(
        'item/<int:pk>',
        MerchstoreDetailView.as_view(),
        name='product'),
    path(
        'item/<int:pk>/edit',
        ProductUpdateView.as_view(),
        name='product_update'),
    path('item/add', ProductCreateView.as_view(), name='product_add'),
    path('cart', CartListView.as_view(), name='cart'),
    path('transactions', TransactionListView.as_view(), name='transactions'),
]

app_name = 'Merchstore'
