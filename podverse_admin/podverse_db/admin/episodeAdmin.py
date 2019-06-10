from django.contrib import admin
from podverse_db.models import Episode

admin.site.site_header = 'Database Admin'
admin.site.index_title = 'Podverse'
admin.site.site_title = 'Admin'

class EpisodeAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'isPublic', 'description', 'duration', 'episodeType', 'guid', 'imageUrl',
              'isExplicit', 'linkUrl', 'mediaFilesize', 'mediaType', 'mediaUrl', 'pastHourTotalUniquePageviews',
              'pastDayTotalUniquePageviews', 'pastWeekTotalUniquePageviews', 'pastMonthTotalUniquePageviews',
              'pastYearTotalUniquePageviews', 'pastAllTimeTotalUniquePageviews', 'pubDate', 'createdAt', 'updatedAt',)
    list_display = ('title', 'id', 'isPublic',)
    list_editable = ('isPublic',)
    ordering = ('-updatedAt',)
    search_fields = ('title', 'id',)

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        if request.user.is_staff:
            if request.user.is_superuser:
                return ['createdAt', 'updatedAt']
            elif request.user.groups.filter(name='Admin').exists():
                fields.remove('isPublic')
                return fields
            elif request.user.groups.filter(name='Curator').exists():
                fields = [f.name for f in self.model._meta.fields]
                fields.remove('isPublic')
                return fields
        else:
            return fields


admin.site.register(Episode, EpisodeAdmin)
