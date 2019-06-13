from django.contrib import admin
from podverse_db.models import Playlist

class PlaylistAdmin(admin.ModelAdmin):
    fields = ('id', 'owner', 'title', 'description', 'isPublic', 'itemCount', 'createdAt', 'updatedAt',)
    list_display = ('id', 'get_owner_email', 'title',)
    ordering = ('-updatedAt',)
    search_fields = ('id', 'title',)

    def get_owner_email(self, obj):
        return obj.owner.email
    get_owner_email.short_description = 'Owner Email'

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

admin.site.register(Playlist, PlaylistAdmin)
