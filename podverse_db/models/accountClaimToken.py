import uuid
from django.db import models

class AccountClaimToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    claimed = models.BooleanField(default=False)
    email = models.CharField(max_length=2084)
    yearsToAdd = models.PositiveIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        managed: False
        db_table = 'accountClaimToken'
        verbose_name = 'AccountClaimToken'
        verbose_name_plural = 'AccountClaimTokens'

    def __str__(self):
        return str(self.id)
