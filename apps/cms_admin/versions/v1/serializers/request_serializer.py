from rest_framework import serializers

from apps.cms_admin.models import IMAGE_TYPE


class AddNewCategoryRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=255, required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UpdateCategoryRequestSerializer(serializers.Serializer):
    category_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(max_length=255, required=False)

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


class AddNewItemRequestSerializer(serializers.Serializer):
    category_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    image = serializers.JSONField(required=False)
    short_description = serializers.CharField(max_length=255, required=False)
    price_temp = serializers.IntegerField(default=0)
    price = serializers.IntegerField(default=0)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UpdateItemRequestSerializer(serializers.Serializer):
    item_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    short_description = serializers.CharField(max_length=255, required=False)
    image = serializers.JSONField(required=False)
    price_temp = serializers.IntegerField(default=0)
    price = serializers.IntegerField(default=0)

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