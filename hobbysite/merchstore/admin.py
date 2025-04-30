from django.contrib import admin
from .models import Product, ProductType

# Register your models here.


class ProductInline(admin.TabularInline):
    model = Product
    fields = [('name', 'price'), 'description']


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInline,]


admin.site.register(ProductType, ProductTypeAdmin)
