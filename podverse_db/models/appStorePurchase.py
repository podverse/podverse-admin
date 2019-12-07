from django.db import models
from .user import User

class AppStorePurchase(models.Model):
    transactionId = models.CharField(max_length=2084, primary_key=True)
    cancellation_date = models.CharField(max_length=2084, blank=True)
    cancellation_date_ms = models.CharField(max_length=2084, blank=True)
    cancellation_date_pst = models.CharField(max_length=2084, blank=True)
    cancellation_reason = models.CharField(max_length=2084, blank=True)
    expires_date = models.CharField(max_length=2084, blank=True)
    expires_date_ms = models.CharField(max_length=2084, blank=True)
    expires_date_pst = models.CharField(max_length=2084, blank=True)
    is_in_intro_offer_period = models.BooleanField(blank=True)
    is_trial_period = models.BooleanField(blank=True)
    original_purchase_date = models.CharField(max_length=2084, blank=True)
    original_purchase_date_ms = models.CharField(max_length=2084, blank=True)
    original_purchase_date_pst = models.CharField(max_length=2084, blank=True)
    original_transaction_id = models.CharField(max_length=2084, blank=True)
    product_id = models.CharField(max_length=2084, blank=True)
    promotional_offer_id = models.CharField(max_length=2084, blank=True)
    purchase_date = models.CharField(max_length=2084, blank=True)
    purchase_date_ms = models.CharField(max_length=2084, blank=True)
    purchase_date_pst = models.CharField(max_length=2084, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    transaction_id = models.CharField(max_length=2084, blank=True)
    web_order_line_item_id = models.CharField(max_length=2084, blank=True)

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column='ownerId')

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'appStorePurchases'
        verbose_name = 'AppStorePurchase'
        verbose_name_plural = 'AppStorePurchases'

    def __str__(self):
        return self.transactionId
