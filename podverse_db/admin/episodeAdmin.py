from django.contrib import admin
from podverse_db.models import Episode

class EpisodeAdmin(admin.ModelAdmin):
    fields = ('id', 'podcast', 'title', 'isPublic', 'description', 'duration', 'episodeType', 'guid', 'imageUrl',
        'isExplicit', 'linkUrl', 'mediaFilesize', 'mediaType', 'mediaUrl', 'pastHourTotalUniquePageviews',
        'pastDayTotalUniquePageviews', 'pastWeekTotalUniquePageviews', 'pastMonthTotalUniquePageviews',
        'pastYearTotalUniquePageviews', 'pastAllTimeTotalUniquePageviews', 'pubDate', 'createdAt', 'updatedAt',)
    list_display = ('title', 'id', 'get_podcast_title', 'get_podcast_id', 'pubDate', 'isPublic',)
    list_editable = ('isPublic',)
    ordering = ('-updatedAt',)
    search_fields = ('id', 'title',)
    autocomplete_fields = ('podcast',)

    def get_podcast_title(self, obj):
        return obj.podcast.title
    get_podcast_title.short_description = 'Podcast Title'

    def get_podcast_id(self, obj):
        return obj.podcast.id
    get_podcast_id.short_description = 'Podcast ID'

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        if request.user.is_superuser:
            return ['createdAt', 'updatedAt']
        else:
            return fields

admin.site.register(Episode, EpisodeAdmin)
