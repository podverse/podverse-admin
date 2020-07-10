from django.contrib import admin
from podverse_db.models import Category

class CategoryAdmin(admin.ModelAdmin):
    fields = ('id', 'category', 'title', 'fullPath', 'slug', 'createdAt', 'updatedAt',)
    list_display = ('id', 'title', 'fullPath', 'slug')
    ordering = ('-updatedAt',)
    search_fields = ('id', 'title',)
    autocomplete_fields = ('category',)

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        if request.user.is_superuser:
            return ['createdAt', 'updatedAt']
        else:
            return fields

admin.site.register(Category, CategoryAdmin)
