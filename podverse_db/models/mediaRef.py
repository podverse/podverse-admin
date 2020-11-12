from django.db import models
from .episode import Episode
from .user import User

class MediaRef(models.Model):
    id = models.CharField(max_length=14, primary_key=True)

    endTime = models.PositiveIntegerField(default=0, blank=True)
    imageUrl = models.CharField(max_length=2084, blank=True)
    isOfficialChapter = models.BooleanField(default=False)
    isOfficialSoundBite = models.BooleanField(default=False)
    isPublic = models.BooleanField(default=False)
    linkUrl = models.CharField(max_length=2084, blank=True)
    pastHourTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Hour')
    pastDayTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Day')
    pastWeekTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Week')
    pastMonthTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Month')
    pastYearTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - Past Year')
    pastAllTimeTotalUniquePageviews = models.PositiveIntegerField(default=0, verbose_name='Pageviews - All Time')
    startTime = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=2084, blank=True)

    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, db_column='episodeId')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_column='ownerId')

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'mediaRefs'
        verbose_name = 'MediaRef'
        verbose_name_plural = 'MediaRefs'

    def __str__(self):
        return self.id
