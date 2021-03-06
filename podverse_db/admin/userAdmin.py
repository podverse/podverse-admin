import bcrypt
import shortuuid
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from podverse_db.models import User
from podverse_admin.scripts.mailer import sendNewUserEmail

class UserAdmin(admin.ModelAdmin):
    user_fields = ['id', 'email', 'emailVerified', 'freeTrialExpiration', 'isPublic', 'membershipExpiration',
        'name', 'roles', 'createdAt', 'updatedAt',]

    fields = user_fields
    list_display = ('id', 'obscured_email', 'obscured_name',)
    ordering = ('-updatedAt',)
    search_fields = ('id', 'obscured_email', 'obscured_name')

    def obscured_email(self, obj):
        return obj.email[0:3] + '***************'
    obscured_email.short_description = 'Email'

    def obscured_name(self, obj):
        return obj.name[0:3] + '***************' if isinstance(obj.name, str) and len(obj.name) > 3 else '******************'
    obscured_name.short_description = 'Name'

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        if request.user.is_superuser:
            return ['createdAt', 'updatedAt']
        elif request.user.groups.filter(name='Admin').exists():
            return ['createdAt', 'updatedAt']
        else:
            return fields

    def get_form(self, request, obj=None, **kwargs):
        self.fields =self.user_fields
        form = super(UserAdmin, self).get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):
        # If is a new user, then randomly generate a password for them.
        # To log into their account, they will need to use Reset Password.
        if not change:
            password = shortuuid.ShortUUID().random(length=14)
            obj.password = bcrypt.hashpw(password, bcrypt.gensalt())
        super(UserAdmin, self).save_model(request, obj, form, change)


def handlePostSave(sender, instance, **kwargs):
    if kwargs.get('created'):
        sendNewUserEmail(instance.email)

post_save.connect(handlePostSave, sender=User)

admin.site.register(User, UserAdmin)
