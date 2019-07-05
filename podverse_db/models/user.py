from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
import shortuuid

class User(models.Model):
    def shortid():
        return shortuuid.ShortUUID().random(length=7)

    id = models.CharField(max_length=14, primary_key=True, default=shortid)

    email = models.EmailField(unique=True)
    emailVerified = models.BooleanField()
    freeTrialExpiration = models.DateTimeField(blank=True)
    isPublic = models.BooleanField(default=False)
    membershipExpiration = models.DateTimeField(blank=True)
    name = models.CharField(max_length=2084, blank=True)
    password = models.CharField(max_length=2084)
    roles = ArrayField(
        models.CharField(max_length=2084),
        size=20,
        default=list,
        blank=True
    )
    historyItems = JSONField(default=list, blank=True)
    queueItems = JSONField(default=list, blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'users'

    def __str__(self):
        return self.email
