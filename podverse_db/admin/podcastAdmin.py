from django.contrib import admin
from podverse_db.models import FeedUrl, Podcast

class FeedUrlInline(admin.TabularInline):
    model = FeedUrl
    classes = ['collapse']
    fields = ('id', 'isAuthority', 'url',)
    max_num = 0
    can_delete = False
    extra = 0
    
    def has_add_permission(self, request, obj=None):
        return False

class PodcastAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'isPublic', 'hideDynamicAdsWarning', 'alwaysFullyParse', 'podcastIndexId', 'authorityId', 'description', 'feedLastUpdated',
        'feedLastParseFailed', 'guid', 'imageUrl', 'isExplicit', 'language', 'lastEpisodePubDate', 'lastEpisodeTitle', 'linkUrl',
        'pastHourTotalUniquePageviews', 'pastDayTotalUniquePageviews', 'pastWeekTotalUniquePageviews',
        'pastMonthTotalUniquePageviews', 'pastYearTotalUniquePageviews', 'pastAllTimeTotalUniquePageviews',
        'shrunkImageUrl', 'sortableTitle', 'type', 'createdAt', 'updatedAt',)
    list_display = ('title', 'id', 'podcastIndexId', 'authorityId', 'isPublic', 'hideDynamicAdsWarning', 'alwaysFullyParse', 'feedLastParseFailed',)
    list_editable = ('isPublic', 'hideDynamicAdsWarning', 'alwaysFullyParse', 'feedLastParseFailed',)
    ordering = ('-updatedAt',)
    search_fields = ('id', 'title',)
    inlines = [ FeedUrlInline ]

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        if request.user.is_superuser:
            return ['createdAt', 'updatedAt']
        elif request.user.groups.filter(name='Admin').exists():
            fields.remove('isPublic')
            fields.remove('title')
            fields.remove('podcastIndexId')
            fields.remove('authorityId')
            fields.remove('hideDynamicAdsWarning')
            fields.remove('alwaysFullyParse')
            return fields
        elif request.user.groups.filter(name='Curator').exists():
            fields.remove('isPublic')
            fields.remove('title')
            fields.remove('podcastIndexId')
            fields.remove('authorityId')
            fields.remove('hideDynamicAdsWarning')
            fields.remove('alwaysFullyParse')
            return fields
        else:
            return fields

admin.site.register(Podcast, PodcastAdmin)
