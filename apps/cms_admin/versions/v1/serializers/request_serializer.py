from rest_framework import serializers

from apps.cms_admin.models import IMAGE_TYPE


class AddNewCategoryRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=1024, required=True)
    description = serializers.CharField(max_length=10000, required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UpdateCategoryRequestSerializer(serializers.Serializer):
    category_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=1024, required=False)
    description = serializers.CharField(max_length=10000, required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DeleteCategoryRequestSerializer(serializers.Serializer):
    category_id = serializers.ListField(child=serializers.IntegerField(min_value=0, required=True), required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UploadImageItemRequestSerializer(serializers.Serializer):
    image = serializers.ImageField(required=False)
    type = serializers.ChoiceField(IMAGE_TYPE, required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AddNewSupplierRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=1024, required=True)
    description = serializers.CharField(max_length=10000, required=False)
    address = serializers.CharField(max_length=1024, required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UpdateSupplierRequestSerializer(serializers.Serializer):
    supplier_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=1024, required=False)
    description = serializers.CharField(max_length=10000, required=False)
    address = serializers.CharField(max_length=1024, required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DeleteSupplierRequestSerializer(serializers.Serializer):
    supplier_id = serializers.ListField(child=serializers.IntegerField(min_value=0, required=True), required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AddNewItemRequestSerializer(serializers.Serializer):
    category_id = serializers.IntegerField(required=True)
    supplier_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=1024)
    quantity = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length=10000)
    image = serializers.JSONField(required=False)
    short_description = serializers.CharField(max_length=10000, required=False)
    price_temp = serializers.IntegerField(default=0)
    price = serializers.IntegerField(default=0)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UpdateItemRequestSerializer(serializers.Serializer):
    item_id = serializers.IntegerField(required=True)
    category_id = serializers.IntegerField(required=True)
    supplier_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=1024)
    description = serializers.CharField(max_length=10000)
    short_description = serializers.CharField(max_length=10000, required=False)
    image = serializers.JSONField(required=False)
    quantity = serializers.IntegerField(required=True)
    price_temp = serializers.IntegerField(default=0)
    price = serializers.IntegerField(default=0)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UpdateQuantityRequestSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DeleteItemRequestSerializer(serializers.Serializer):
    item_id = serializers.ListField(child=serializers.IntegerField(min_value=0, required=True), required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AddNewOrderRequestSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=0)
    user_name = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=1024)
    phone = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UpdateOrderRequestSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    status = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AddNewCommentRequestSerializer(serializers.Serializer):
    comment = serializers.CharField(max_length=10000, required=True)
    item_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    rating = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UpdateCommentRequestSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField(required=True)
    comment = serializers.CharField(max_length=10000, required=True)
    item_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    rating = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DeleteCommentRequestSerializer(serializers.Serializer):
    comment_id = serializers.ListField(child=serializers.IntegerField(min_value=0, required=True), required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
