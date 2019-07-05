from django.contrib import admin
from podverse_db.models import User
import bcrypt

class UserAdmin(admin.ModelAdmin):
    user_fields = ['id', 'email', 'emailVerified', 'freeTrialExpiration', 'isPublic', 'membershipExpiration',
        'name', 'roles', 'createdAt', 'updatedAt',]

    fields = user_fields
    list_display = ('id', 'email', 'name',)
    ordering = ('-updatedAt',)
    search_fields = ('id', 'email', 'name')

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        if request.user.is_superuser:
            return ['createdAt', 'updatedAt']
        else:
            return fields

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            superuser_fields = self.user_fields + ['password']
            self.fields = superuser_fields
        else:
            self.fields = self.user_fields
            self.exclude = ['password']
        form = super(UserAdmin, self).get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):
        obj.password = bcrypt.hashpw(obj.password, bcrypt.gensalt())
        super(UserAdmin, self).save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)
