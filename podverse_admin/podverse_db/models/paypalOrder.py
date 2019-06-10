from django.db import models
from .user import User

class PayPalOrder(models.Model):
    paymentID = models.CharField(max_length=2084, primary_key=True)
    state = models.CharField(max_length=2084, blank=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_column='ownerId')

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'paypalOrder'
        verbose_name = 'PayPalOrder'
        verbose_name_plural = 'PayPalOrders'

    def __str__(self):
        return self.paymentID
