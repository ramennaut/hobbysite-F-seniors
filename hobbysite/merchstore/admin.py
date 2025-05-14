from django.contrib import admin
from .models import Product, ProductType, Transaction

# Register your models here.


class ProductInline(admin.TabularInline):
    model = Product
    fieldsets = [
        (
            None,
            {
                "fields": [
                    ('name', 'price', 'stock'),
                    'status',
                    'owner',
                    'description'
                ]
            }
        )
    ]


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInline,]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    '''Admin View for Transaction'''


admin.site.register(ProductType, ProductTypeAdmin)
