from django.db import models
from .user import User

class BitPayInvoice(models.Model):
    id = models.CharField(max_length=14, primary_key=True)

    orderId = models.CharField(max_length=2084, unique=True)
    amountPaid = models.IntegerField(default=0)
    currency = models.CharField(max_length=2084)
    exceptionStatus = models.CharField(max_length=2084, default='false')
    price = models.IntegerField()
    status = models.CharField(max_length=2084, blank=True)
    transactionCurrency = models.CharField(max_length=2084, blank=True)
    transactionSpeed = models.CharField(max_length=2084, blank=True)
    url = models.URLField()

    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_column='ownerId')

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'bitpayInvoice'
        verbose_name = 'BitPayInvoice'
        verbose_name_plural = 'BitPayInvoices'

    def __str__(self):
        return self.id
