
from django.contrib import admin
from podverse_db.models import BitPayInvoice

admin.site.site_header = 'Database Admin'
admin.site.index_title = 'Podverse'
admin.site.site_title = 'Admin'

class BitPayInvoiceAdmin(admin.ModelAdmin):
    fields = ('id', 'orderId', 'owner', 'amountPaid', 'currency', 'exceptionStatus', 'price', 'status',
      'transactionCurrency', 'transactionSpeed', 'url', 'createdAt', 'updatedAt',)
    list_display = ('id', 'orderId', 'owner')
    ordering = ('-updatedAt',)
    search_fields = ('id', 'orderId')

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        return fields

admin.site.register(BitPayInvoice, BitPayInvoiceAdmin)