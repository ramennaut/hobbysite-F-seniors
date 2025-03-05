from django.urls import path
from views import MerchstoreDetailView, MerchstoreListView

urlpatterns = [
    path(
        'merchstore/items',
        MerchstoreListView.as_view(),
        name='list-view'),
    path(
        'merchstore/item/<int:pk>',
        MerchstoreDetailView.as_view(),
        name='detail-view'),
]

app_name = 'Merchstore'
