from rest_framework import serializers

from apps.authentication.models import User
from apps.cms_admin.models import Category, Items, Orders, Supplier


class ListUserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'gender', 'birthday', 'is_active', 'created_at']


class ListCategoryResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ListItemResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"


class ListOrderResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class ListSupplierResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
