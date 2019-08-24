from django.contrib import admin
from podverse_db.models import FeedUrl, Podcast

class FeedUrlInline(admin.TabularInline):
    model = FeedUrl
    fields = ('id', 'isAuthority', 'url')
    readonly_fields = ('id',)
    can_delete = False
    extra = 0

class PodcastAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'isPublic', 'description', 'feedLastUpdated', 'guid', 'imageUrl',
        'isExplicit', 'language', 'lastEpisodePubDate', 'lastEpisodeTitle', 'linkUrl', 'pastHourTotalUniquePageviews',
        'pastDayTotalUniquePageviews', 'pastWeekTotalUniquePageviews', 'pastMonthTotalUniquePageviews',
        'pastYearTotalUniquePageviews', 'pastAllTimeTotalUniquePageviews', 'sortableTitle',
        'type', 'createdAt', 'updatedAt',)
    list_display = ('title', 'id', 'isPublic',)
    list_editable = ('isPublic',)
    ordering = ('-updatedAt',)
    search_fields = ('id', 'title',)
    inlines = [ FeedUrlInline ]

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

admin.site.register(Podcast, PodcastAdmin)
