from django.db import models
from .podcast import Podcast

class Episode(models.Model):
    id = models.CharField(max_length=14, primary_key=True)

    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField(default=0)
    episodeType = models.CharField(max_length=2084, blank=True)
    guid = models.CharField(max_length=2084, blank=True)
    imageUrl = models.URLField(blank=True)
    isExplicit = models.BooleanField(default=False)
    isPublic = models.BooleanField(default=False)
    linkUrl = models.URLField(blank=True)
    mediaFilesize = models.PositiveIntegerField(default=0)
    mediaType = models.CharField(max_length=2084, blank=True)
    mediaUrl = models.URLField(unique=True)
    pastHourTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Hour')
    pastDayTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Day')
    pastWeekTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Week')
    pastMonthTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Month')
    pastYearTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Year')
    pastAllTimeTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - All Time')
    pubDate = models.DateTimeField(blank=True)
    title = models.CharField(max_length=2084, blank=True)

    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, db_column='podcastId')

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'episodes'

    def __str__(self):
        return self.title
