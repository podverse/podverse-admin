from django.contrib import admin
from podverse_db.models import BitPayInvoice

admin.site.site_header = 'Database Admin'
admin.site.index_title = 'Podverse'
admin.site.site_title = 'Admin'

class BitPayInvoiceAdmin(admin.ModelAdmin):
    fields = ('id', 'orderId', 'amountPaid', 'currency', 'exceptionStatus', 'price', 'status',
      'transactionCurrency', 'transactionSpeed', 'url', 'createdAt', 'updatedAt',)
    list_display = ('id', 'orderId', 'get_owner_email')
    ordering = ('-updatedAt',)
    search_fields = ('id', 'orderId')

    def get_owner_email(self, obj):
        return obj.owner.email
    get_owner_email.short_description = 'Owner Email'

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        return fields

admin.site.register(BitPayInvoice, BitPayInvoiceAdmin)
