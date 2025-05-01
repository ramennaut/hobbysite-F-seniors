from django.db import models
#from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Article Categories"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    #author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.SET_NULL)
    entry = models.TextField()
    header_image = models.ImageField(upload_to='image/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    #author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']