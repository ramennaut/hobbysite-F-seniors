from django.db import models

class Commission(models.Model):
    # Title - max length is 255 characters
    title = models.CharField(max_length=255)
    # Description - text field 
    description = models.TextField()
    # People Required - should be whole number
    people_required = models.IntegerField()
    # Created On - datetime field, only gets set when the model is created
    created_on = models.DateTimeField(auto_now_add=True)
    # Updated On - datetime field, always updates on last model update
    updated_on = models.DateTimeField(auto_now=True)
    # Commissions should be sorted by the date it was created, in ascending order
    class Meta:
        ordering = ['created_on']
    
class Comment(models.Model):
    # Commission - foreign key to Commission, model deletion is cascaded
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    # Entry - text field
    entry = models.TextField()
    # Created On - datetime field, only gets set when the model is created
    created_on = models.DateTimeField(auto_now_add=True)
    # Updated On - datetime field, always updates on last model update
    updated_on = models.DateTimeField(auto_now=True)
    # Comments should be sorted by the date it was created, in descending order
    class Meta:
        ordering = ['created_on']