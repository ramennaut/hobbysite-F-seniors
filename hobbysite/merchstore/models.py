from django.db import models


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
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('merchstore:product', args=[str(self.pk)])
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Product"
        verbose_name_plural = "Products"
