from django.contrib import admin
from podverse_db.models import User

admin.site.site_header = 'Database Admin'
admin.site.index_title = 'Podverse'
admin.site.site_title = 'Admin'

class UserAdmin(admin.ModelAdmin):
    fields = ('id', 'email', 'emailVerified', 'freeTrialExpiration', 'isPublic', 'membershipExpiration',
        'name', 'roles', 'createdAt', 'updatedAt',)
    list_display = ('id', 'email', 'name',)
    ordering = ('-updatedAt',)
    search_fields = ('id', 'email', 'name')

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        if request.user.is_superuser:
            return ['createdAt', 'updatedAt',]
        else:
            return fields

admin.site.register(User, UserAdmin)
