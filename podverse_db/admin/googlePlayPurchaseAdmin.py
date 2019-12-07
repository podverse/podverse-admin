
from django.contrib import admin
from podverse_db.models import GooglePlayPurchase

class GooglePlayPurchaseAdmin(admin.ModelAdmin):
    fields = ('transactionId', 'owner', 'createdAt', 'updatedAt', 'acknowledgementState', 'consumptionState',
              'developerPayload', 'kind', 'productId', 'purchaseTimeMillis', 'purchaseState',
              'purchaseToken',)
    list_display = ('transactionId', 'owner',)
    ordering = ('-updatedAt',)
    search_fields = ('transactionId',)

    def get_readonly_fields(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields]
        return fields


admin.site.register(GooglePlayPurchase, GooglePlayPurchaseAdmin)
