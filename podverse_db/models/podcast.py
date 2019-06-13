from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Podcast(models.Model):
    id = models.CharField(max_length=14, primary_key=True)

    description = models.TextField(blank=True)
    feedLastUpdated = models.DateTimeField(blank=True)
    guid = models.CharField(max_length=2084, blank=True)
    imageUrl = models.URLField(blank=True)
    isExplicit = models.BooleanField(default=False)
    isPublic = models.BooleanField(default=False)
    language = models.CharField(max_length=2084, blank=True)
    lastEpisodePubDate = models.DateTimeField(blank=True)
    lastEpisodeTitle = models.CharField(max_length=2084, blank=True)
    linkUrl = models.URLField(blank=True)
    pastHourTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Hour')
    pastDayTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Day')
    pastWeekTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Week')
    pastMonthTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Month')
    pastYearTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Year')
    pastAllTimeTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - All Time')
    priority = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sortableTitle = models.CharField(max_length=2084, blank=True)
    title = models.CharField(max_length=2084, blank=True)
    type = models.CharField(max_length=2084, blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed: False
        db_table = 'podcasts'
    
    def __str__(self):
        return self.title

        
