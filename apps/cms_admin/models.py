# from jsonfield import JSONField
from django.db import models
from django.db.models import JSONField

from apps.authentication.models import User
from apps.utils.constants import ImageType, OrderStatusType, PaymentStatusType

IMAGE_TYPE = (
    (ImageType.IMAGE_TYPE_1.value, "ImageType1"),
    (ImageType.IMAGE_TYPE_2.value, "ImageType2"),
    (ImageType.IMAGE_TYPE_3.value, "ImageType3"),
)

ORDER_STATUS_TYPE = (
    (OrderStatusType.INIT.value, "Init"),
    (OrderStatusType.PAYMENT_SUCCESS.value, "Payment success"),
    (OrderStatusType.PAYMENT_FAIL.value, "Payment fail"),
    (OrderStatusType.DELIVERING.value, "Delivering"),
    (OrderStatusType.COMPLETED.value, "Done"),
    (OrderStatusType.REFUND.value, "Refund"),
)

PAYMENT_STATUS_TYPE = (
    (PaymentStatusType.CASH.value, "Cash"),
    (PaymentStatusType.CREDIT_CARD.value, "Credit Card")
)


class Category(models.Model):
    name = models.CharField(max_length=1024, default=None)
    description = models.CharField(max_length=10000, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return '{}'.format(self.id)


class ItemImages(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='image_items/')
    type_image = models.IntegerField(choices=IMAGE_TYPE, default=0)

    class Meta:
        db_table = 'item_images'


class Supplier(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=10000)
    address = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'suppliers'

    def __str__(self):
        return '{}'.format(self.id)


class Items(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=10000)
    short_description = models.CharField(max_length=10000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    image = JSONField(null=True, blank=True)
    image2 = JSONField(null=True, blank=True)
    image3 = JSONField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price_temp = models.IntegerField(default=None)
    sale = models.IntegerField(default=0)
    price = models.IntegerField(default=None)
    view_item = models.IntegerField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'items'

    def __str__(self):
        return '{}'.format(self.id)


class Comments(models.Model):
    header = models.CharField(max_length=10000)
    comment = models.CharField(max_length=10000)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return '{}'.format(self.id)


class Orders(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=ORDER_STATUS_TYPE, default=0)
    payment_type = models.IntegerField(choices=PAYMENT_STATUS_TYPE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return '{}'.format(self.id)


class OrderDetails(models.Model):
    quantity = models.IntegerField(default=None)
    unit_price = models.IntegerField(default=None)
    total_price = models.IntegerField(default=None)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'order_details'

    def __str__(self):
        return '{}'.format(self.id)
