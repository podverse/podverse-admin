from django.contrib import admin
from podverse_db.models import FeedUrl

class FeedUrlAdmin(admin.ModelAdmin):
    fields = ('id', 'podcast', 'isAuthority', 'url', 'createdAt', 'updatedAt',)
    list_display = ('id', 'url', 'get_podcast_title', 'get_podcast_id', 'isAuthority',)
    list_editable = ('isAuthority',)
    ordering = ('-updatedAt',)
    search_fields = ('id', 'url',)
    autocomplete_fields = ('podcast',)
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
        elif request.user.groups.filter(name='Admin').exists():
            fields.remove('isAuthority')
            fields.remove('podcast')
            fields.remove('url')
            return fields
        elif request.user.groups.filter(name='Curator').exists():
            fields.remove('isAuthority')
            fields.remove('podcast')
            fields.remove('url')
            return fields
        else:
            return fields

admin.site.register(FeedUrl, FeedUrlAdmin)
