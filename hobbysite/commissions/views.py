from django.views.generic import ListView, DetailView
from .models import Commission

class commision_list(ListView):
    model = Commission
    template_name = 'commissions/commission_list.html'
    context_object_name = 'commissions'

class commission_detail(DetailView):
    model = Commission
    template_name = 'commissions/commission_detail.html'
    context_object_name = 'commission'