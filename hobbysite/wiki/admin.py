from django.contrib import admin
from .models import ArticleCategory, Article, Comment

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_on', 'updated_on')
    list_filter = ('category', 'created_on', 'author')
    search_fields = ('title', 'entry')
    readonly_fields = ('created_on', 'updated_on')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'created_on', 'updated_on')
    list_filter = ('created_on', 'article')
    search_fields = ('entry', 'author__user__username', 'article__title')
    readonly_fields = ('created_on', 'updated_on')

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

