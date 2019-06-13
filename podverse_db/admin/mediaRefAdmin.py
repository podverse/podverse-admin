from django.contrib import admin
from podverse_db.models import MediaRef

class MediaRefAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'episode', 'owner', 'startTime', 'endTime', 'isPublic', 'pastHourTotalUniquePageviews',
        'pastDayTotalUniquePageviews', 'pastWeekTotalUniquePageviews', 'pastMonthTotalUniquePageviews',
        'pastYearTotalUniquePageviews', 'pastAllTimeTotalUniquePageviews', 'createdAt',
        'updatedAt',)
    list_display = ('id', 'title', 'get_podcast_title', 'get_episode_title', 'isPublic',)
    list_editable = ('isPublic',)
    ordering = ('-updatedAt',)
    search_fields = ('id', 'title',)

    def get_podcast_title(self, obj):
        return obj.episode.podcast.title
    get_podcast_title.short_description = 'Podcast Title'

    def get_episode_title(self, obj):
        return obj.episode.title
    get_episode_title.short_description = 'Episode Title'

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        if request.user.is_superuser:
            return ['createdAt', 'updatedAt']
        elif request.user.groups.filter(name='Admin').exists():
            fields.remove('isPublic')
            return fields
        elif request.user.groups.filter(name='Curator').exists():
            fields.remove('isPublic')
            return fields
        else:
            return fields

admin.site.register(MediaRef, MediaRefAdmin)
