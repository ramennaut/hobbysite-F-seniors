from django.db import models
from user_management.models import Profile


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()

    available = 'Available'
    on_sale = 'On Sale'
    out_of_stock = 'Out of Stock'
    status_choices = (
        (available, 'Available'),
        (on_sale, 'On Sale'),
        (out_of_stock, 'Out of Stock'),
    )
    status = models.CharField(choices=status_choices, max_length=255)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('Merchstore:product', args=[str(self.pk)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Transaction(models.Model):
    '''Model definition for Transaction.'''
    buyer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()

    on_cart = 'On Cart'
    to_pay = 'To Pay'
    to_ship = 'To Ship'
    to_receive = 'To Receive'
    delivered = 'Delivered'
    status_choices = (
        (on_cart, 'On Cart'),
        (to_pay, 'To Pay'),
        (to_ship, 'To Ship'),
        (to_receive, 'To Receive'),
        (delivered, 'Delivered'),
    )
    status = models.CharField(choices=status_choices, max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''Meta definition for Transaction.'''

        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return self.buyer.name + ' - ' + self.product.name + ' (' + self.status + ')'
