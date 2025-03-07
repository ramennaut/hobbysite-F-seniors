from django.contrib import admin
from .models import Commission, Comment

class CommissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'people_required', 'created_on', 'updated_on')
    list_filter = ('created_on',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commission', 'created_on', 'updated_on')
    list_filter = ('created_on',)

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)