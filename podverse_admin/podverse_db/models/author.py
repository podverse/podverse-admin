from django.db import models

class Author(models.Model):
    id = models.CharField(max_length=14, primary_key=True)

    name = models.CharField(max_length=2084, unique=True)
    slug = models.CharField(max_length=2084, unique=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'authors'

    def __str__(self):
        return self.name
