from django.contrib import admin
from podverse_db.models import Author

admin.site.site_header = 'Database Admin'
admin.site.index_title = 'Podverse'
admin.site.site_title = 'Admin'

class AuthorAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'slug', 'createdAt', 'updatedAt',)
    list_display = ('id', 'name', 'slug',)
    ordering = ('-updatedAt',)
    search_fields = ('id', 'name', 'slug',)

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        if request.user.is_superuser:
            return ['createdAt', 'updatedAt']
        else:
            return fields

admin.site.register(Author, AuthorAdmin)
