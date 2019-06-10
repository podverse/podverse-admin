from django.contrib import admin
from podverse_db.models import PayPalOrder

admin.site.site_header = 'Database Admin'
admin.site.index_title = 'Podverse'
admin.site.site_title = 'Admin'

class PayPalOrderAdmin(admin.ModelAdmin):
    fields = ('paymentID', 'state', 'owner', 'createdAt', 'updatedAt',)
    list_display = ('paymentID', 'state', 'get_owner_email')
    ordering = ('-updatedAt',)
    search_fields = ('paymentID',)

    def get_owner_email(self, obj):
        return obj.owner.email
    get_owner_email.short_description = 'Owner Email'

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        return fields

admin.site.register(PayPalOrder, PayPalOrderAdmin)
