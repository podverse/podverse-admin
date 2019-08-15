from django.db import models
from .podcast import Podcast
import shortuuid

class FeedUrl(models.Model):
    def shortid():
        return shortuuid.ShortUUID().random(length=14)

    id = models.CharField(max_length=14, primary_key=True, default=shortid)

    isAuthority = models.BooleanField(default=True)
    url = models.URLField(unique=True)

    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, db_column='podcastId', blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'feedUrls'
        verbose_name = 'FeedUrl'
        verbose_name_plural = 'FeedUrls'

    def __str__(self):
        return self.id
