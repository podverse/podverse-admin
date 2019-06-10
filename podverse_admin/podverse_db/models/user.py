from django.contrib.postgres.fields import ArrayField
from django.db import models

class User(models.Model):
    id = models.CharField(max_length=14, primary_key=True)

    email = models.EmailField(unique=True)
    emailVerified = models.BooleanField()
    freeTrialExpiration = models.DateTimeField(blank=True)
    isPublic = models.BooleanField()
    membershipExpiration = models.DateTimeField(blank=True)
    name = models.CharField(max_length=2084, blank=True)
    roles = ArrayField(
        models.CharField(max_length=2084),
        size=20,
        default=list
    )
    subscribedPlaylistIds = ArrayField(
        models.CharField(max_length=14),
        size=20,
        default=list
    )
    subscribedPodcastIds = ArrayField(
        models.CharField(max_length=14),
        size=20,
        default=list
    )
    subscribedUserIds = ArrayField(
        models.CharField(max_length=14),
        size=20,
        default=list
    )   

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'users'

    def __str__(self):
        return self.email
