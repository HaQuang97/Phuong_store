# from jsonfield import JSONField
from django.db import models
from django.db.models import JSONField

from apps.authentication.models import User
from apps.cms_admin.models import Items
from apps.utils.constants import OrderStatusType

ORDER_STATUS_TYPE = (
    (OrderStatusType.INIT.value, "Init"),
    (OrderStatusType.PAYMENT_SUCCESS.value, "Payment success"),
    (OrderStatusType.PAYMENT_FAIL.value, "Payment fail"),
    (OrderStatusType.DELIVERING.value, "Delivering"),
    (OrderStatusType.COMPLETED.value, "Done"),
    (OrderStatusType.REFUND.value, "Refund"),
)


class CreditCard(models.Model):
    full_name = models.CharField(max_length=255)
    number_credit = models.CharField(max_length=20)
    expire_date = models.DateField()
    CVV = models.IntegerField()
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'credit_card'

    def __str__(self):
        return '{}'.format(self.id)


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, unique=True, max_length=70, null=True)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return '{}'.format(self.id)
