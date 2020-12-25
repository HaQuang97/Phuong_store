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
    address = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'credit_card'

    def __str__(self):
        return '{}'.format(self.id)


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, max_length=70, null=True)
    body = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return '{}'.format(self.id)


class Subscribers(models.Model):
    email = models.EmailField(blank=True, max_length=70, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'subscribers'

    def __str__(self):
        return '{}'.format(self.id)


class Blogs(models.Model):
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=10000)
    author = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    like = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'blogs'

    def __str__(self):
        return '{}'.format(self.id)


class Carts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'carts'

    def __str__(self):
        return '{}'.format(self.id)


class CartItems(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'cart_items'

    def __str__(self):
        return '{}'.format(self.id)
