from django.db import models

from apps.authentication.models import User


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


class Items(models.Model):
    name = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None)
    short_description = models.CharField(max_length=255, default=None)
    image1 = models.ImageField(null=True, blank=True, upload_to='image_items/')
    image2 = models.ImageField(null=True, blank=True, upload_to='image_items/')
    image3 = models.ImageField(null=True, blank=True, upload_to='image_items/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    phone = models.IntegerField(default=None)
    address = models.CharField(max_length=255, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
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
