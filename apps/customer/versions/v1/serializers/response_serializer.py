from rest_framework import serializers

from apps.authentication.models import User
from apps.cms_admin.models import Category, Items, Orders, Supplier, Comments


class ListUserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'gender', 'birthday', 'is_active', 'created_at']


class ListCategoryResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ListItemResponseSerializer(serializers.ModelSerializer):
    category = ListCategoryResponseSerializer()
    category2 = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ('category','category2')

    def get_category2(self, obj):
        return obj.name.lowwer()


class ListCommentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class ListOrderResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class ListSupplierResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = "__all__"
