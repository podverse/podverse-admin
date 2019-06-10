from django.db import models
from .podcast import Podcast

class FeedUrl(models.Model):
    id = models.CharField(max_length=14, primary_key=True)

    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, db_column='podcastId')

    isAuthority = models.BooleanField()
    url = models.URLField(unique=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'feedUrls'

    def __str__(self):
        return self.id
