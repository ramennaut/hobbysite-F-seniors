from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product


class MerchstoreListView(ListView):
    model = Product
    template_name = 'product_list_view.html'


class MerchstoreDetailView(DetailView):
    model = Product
    template_name = 'product_detail_view.html'

