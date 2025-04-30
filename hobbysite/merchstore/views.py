from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product


class MerchstoreListView(ListView):
    model = Product
    template_name = 'list_view.html'


class MerchstoreDetailView(DetailView):
    model = Product
    template_name = 'detail_view.html'

