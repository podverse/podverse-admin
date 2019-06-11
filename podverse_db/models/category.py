from django.db import models
from .podcast import Podcast

class Category(models.Model):
    id = models.CharField(max_length=14, primary_key=True)
    
    fullPath = models.CharField(max_length=2084, unique=True)
    slug = models.CharField(max_length=2084)
    title = models.CharField(max_length=2084, unique=True)

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, db_column='categoryId', related_name='category_category', null=True, blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
