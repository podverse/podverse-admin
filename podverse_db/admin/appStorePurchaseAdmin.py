
from django.contrib import admin
from podverse_db.models import AppStorePurchase

class AppStorePurchaseAdmin(admin.ModelAdmin):
    fields = ('transactionId', 'owner', 'createdAt', 'updatedAt', 'cancellation_date', 'cancellation_date_ms',
        'cancellation_date_pst','cancellation_reason', 'expires_date', 'expires_date_ms', 'expires_date_pst',
        'is_in_intro_offer_period', 'is_trial_period', 'original_purchase_date', 'original_purchase_date_ms',
        'original_purchase_date_pst', 'original_transaction_id', 'product_id', 'promotional_offer_id',
        'purchase_date', 'purchase_date_ms', 'purchase_date_pst', 'quantity', 'transaction_id',
        'web_order_line_item_id',)
    list_display = ('transactionId', 'owner',)
    ordering = ('-updatedAt',)
    search_fields = ('transactionId',)
    raw_id_fields = ('owner',)

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        return fields

admin.site.register(AppStorePurchase, AppStorePurchaseAdmin)
