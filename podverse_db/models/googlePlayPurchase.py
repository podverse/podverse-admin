from django.db import models
from .user import User


class GooglePlayPurchase(models.Model):
    transactionId = models.CharField(max_length=2084, primary_key=True)
    acknowledgementState = models.IntegerField(blank=True)
    consumptionState = models.IntegerField(blank=True)
    developerPayload = models.CharField(max_length=2084, blank=True)
    kind = models.CharField(max_length=2084, blank=True)
    productId = models.CharField(max_length=2084)
    purchaseTimeMillis = models.CharField(max_length=2084, blank=True)
    purchaseState = models.IntegerField(blank=True)
    purchaseToken = models.CharField(max_length=2084, unique=True)

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column='ownerId')

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'googlePlayPurchases'
        verbose_name = 'GooglePlayPurchase'
        verbose_name_plural = 'GooglePlayPurchases'

    def __str__(self):
        return self.transactionId
