from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('merchstore:product', args=[str(self.pk)])

    class Meta:
        ordering = ['name']
