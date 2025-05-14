from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from user_management.models import Profile

from .forms import ProductForm, TransactionForm
from .models import Product, Transaction


class MerchstoreListView(ListView):
    model = Product
    template_name = 'list_view.html'

    # Overloaded Function
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_products = Product.objects.order_by('name')

        if self.request.user.is_authenticated:
            user = Profile.objects.get(user=self.request.user)
            user_products = all_products.filter(
                owner=user
            )
            context['user_products'] = user_products

            all_products = all_products.exclude(
                owner=user
            )

        context['all_products'] = all_products
        return context


class MerchstoreDetailView(DetailView):
    model = Product
    template_name = 'detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = None
        if self.request.user.is_authenticated:
            user = Profile.objects.get(user=self.request.user)
            context['user'] = user

        context['transaction_form'] = TransactionForm(initial={
            'buyer': user,
            'product': context['object'],
            'amount': 1,
        })
        context['pk'] = self.kwargs['pk']
        return context

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        form = TransactionForm(request.POST)

        if form.is_valid():
            if request.user.is_authenticated:
                user = Profile.objects.get(user=self.request.user)
                transaction = form.save(commit=False)
                transaction.buyer = user
                transaction.product = product
                transaction.status = Transaction.on_cart
                transaction.save()
                if product.stock - transaction.amount < 0:
                    return self.get(request, *args, **kwargs)
                product.stock -= transaction.amount
                if product.stock <= 0:
                    product.status = Product.out_of_stock
                product.save()

                return redirect('Merchstore:cart')
            else:
                # !! should eventually redirect to the login page
                return redirect('admin:login')

        return self.get(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_view.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        print(form.fields['owner'].__dir__())

        user = None
        if self.request.user.is_authenticated:
            user = Profile.objects.get(user=self.request.user)
        form.fields['owner'].initial = user
        form.fields['owner'].disabled = True
        form.fields['price'].initial = 0.00
        form.fields['stock'].initial = 1
        form.fields['status'].initial = Product.available
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = None
        if self.request.user.is_authenticated:
            user = Profile.objects.get(user=self.request.user)
            context['user'] = user
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_view.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['owner'].disabled = True
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


class CartListView(ListView):
    model = Transaction
    template_name = 'cart_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = Profile.objects.get(user=self.request.user)
        transactions = Transaction.objects.filter(buyer=user)
        print(transactions)

        cart = {}
        for transaction in transactions:
            if not cart.__contains__(transaction.product.owner):
                cart[transaction.product.owner] = []
            cart[transaction.product.owner].append(transaction)

        context['cart'] = cart

        return context


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = Profile.objects.get(user=self.request.user)

        transactions = Transaction.objects.filter(product__owner=user)

        transaction_list = {}
        for transaction in transactions:
            if not transaction_list.__contains__(transaction.buyer):
                transaction_list[transaction.buyer] = []
            transaction_list[transaction.buyer].append(transaction)
            print(transaction.status)

        context['transaction_list'] = transaction_list

        return context
