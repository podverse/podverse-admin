
from django.contrib import admin
from podverse_db.models import AccountClaimToken

class AccountClaimTokenAdmin(admin.ModelAdmin):
    fields = ('id', 'claimed', 'email', 'yearsToAdd', 'createdAt', 'updatedAt',)
    list_display = ('id', 'claimed', 'email', 'yearsToAdd',)
    ordering = ('-updatedAt',)
    search_fields = ('id', 'email',)

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        if request.user.is_superuser:
            return ['id', 'createdAt', 'updatedAt']
        elif request.user.groups.filter(name='Admin').exists():
            fields.remove('claimed')
            fields.remove('email')
            fields.remove('yearsToAdd')
            return fields
        else:
            return fields

admin.site.register(AccountClaimToken, AccountClaimTokenAdmin)
