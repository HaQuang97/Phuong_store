# from jsonfield import JSONField
from django.db import models
from django.db.models import JSONField

from apps.authentication.models import User
from apps.utils.constants import ImageType, OrderStatusType

IMAGE_TYPE = (
    (ImageType.IMAGE_TYPE_1.value, "ImageType1"),
    (ImageType.IMAGE_TYPE_2.value, "ImageType2"),
    (ImageType.IMAGE_TYPE_3.value, "ImageType3"),
)

ORDER_STATUS_TYPE = (
    (OrderStatusType.WAIT_ACCEPT.value, "WaitAccept"),
    (OrderStatusType.ACCEPT.value, "Accept"),
    (OrderStatusType.SUCCESS.value, "Success"),
)


class Category(models.Model):
    name = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None)
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


class Items(models.Model):
    name = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None)
    short_description = models.CharField(max_length=255, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = JSONField(null=True, blank=True)
    price_temp = models.IntegerField(default=None)
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
    comment = models.CharField(max_length=255, default=None)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return '{}'.format(self.id)


class Orders(models.Model):
    name = models.CharField(max_length=255, default=None)
    phone = models.IntegerField(default=None)
    address = models.CharField(max_length=255, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=ORDER_STATUS_TYPE, default=1)
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
