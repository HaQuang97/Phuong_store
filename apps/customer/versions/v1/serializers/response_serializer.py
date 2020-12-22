from rest_framework import serializers

from apps.authentication.models import User
from apps.customer.models import Contact, CreditCard


# class ListItemResponseSerializer(serializers.ModelSerializer):
#     category = ListCategoryResponseSerializer()
#     category2 = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Items
#         fields = ('category','category2')
#
#     def get_category2(self, obj):
#         return obj.name.lowwer()

class ListUserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'gender', 'birthday', 'is_active', 'created_at']


class ListContactResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
