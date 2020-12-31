from rest_framework import serializers

from apps.authentication.models import User
from apps.cms_admin.models import Category, Items, Orders, Supplier, Comments, OrderDetails


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


class ListOrderDetailResponseSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    item = serializers.SerializerMethodField()
    # quantity = serializers.SerializerMethodField()
    class Meta:
        model = Orders
        fields = ['id', 'name', 'phone', 'address', 'total_price', 'status', 'payment_type', 'item']

    def get_total_price(self, obj):
        total_bill = 0
        total_bill = total_bill + obj.orderdetails_data[0].total_price
        return total_bill

    def get_item(self, obj):
        list_item = []
        if obj.orderdetails_data:
            for i in obj.orderdetails_data:
                res = {
                    'item_id': i.item_id,
                    'name': i.item.name,
                    'description': i.item.description,
                    'short_description': i.item.short_description,
                    'image': i.item.image,
                    'price': i.item.price,
                    'quantity': i.item.quantity,
                    'total_price_item': i.item.quantity * i.item.price
                }
                list_item.append(res)
        return list_item
