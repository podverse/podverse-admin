from django.contrib import admin
from podverse_db.models import FeedUrl

admin.site.site_header = 'Database Admin'
admin.site.index_title = 'Podverse'
admin.site.site_title = 'Admin'

class FeedUrlAdmin(admin.ModelAdmin):
    fields = ('id', 'podcast', 'isAuthority', 'url', 'createdAt', 'updatedAt',)
    list_display = ('id', 'get_podcast_title', 'url', 'isAuthority',)
    list_editable = ('isAuthority',)
    ordering = ('-updatedAt',)
    search_fields = ('url', 'id',)

    def get_podcast_title(self, obj):
        return obj.podcast.title
    get_podcast_title.short_description = 'Podcast Title'

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        if request.user.is_staff:
            if request.user.is_superuser:
                return ['createdAt', 'updatedAt']
            elif request.user.groups.filter(name='Admin').exists():
                fields.remove('isAuthority')
                fields.remove('url')
                return fields
            elif request.user.groups.filter(name='Curator').exists():
                fields = [f.name for f in self.model._meta.fields]
                fields.remove('isAuthority')
                fields.remove('url')
                return fields
        else:
            return fields


admin.site.register(FeedUrl, FeedUrlAdmin)
