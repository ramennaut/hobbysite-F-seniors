from django import forms
from .models import Product, Transaction


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'name',
            'product_type',
            'owner',
            'description',
            'price',
            'stock',
            'status'
        )


class TransactionForm(forms.ModelForm):
    # buyer = forms.CharField(disabled=True)
    # product = forms.CharField(disabled=True)

    class Meta:
        model = Transaction
        fields = ('buyer', 'product', 'amount',)
