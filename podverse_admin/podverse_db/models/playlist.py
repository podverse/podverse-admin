from django.db import models
from .user import User

class Playlist(models.Model):
    id = models.CharField(max_length=14, primary_key=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_column='ownerId')

    description = models.CharField(max_length=2084, blank=True)
    isPublic = models.BooleanField()
    itemCount = models.IntegerField(default=0, blank=True)
    title = models.CharField(max_length=2084, blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'playlists'

    def __str__(self):
        return self.id
