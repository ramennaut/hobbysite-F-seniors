from django.db import models
from django.urls import reverse

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

createdOn = models.DateTimeField(auto_now_add=True)
updatedOn = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ['-createdOn']

def __str__(self):
    return self.title
