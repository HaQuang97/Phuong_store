from rest_framework import serializers

from apps.authentication.models import User
from apps.customer.models import Contact, CreditCard, Subscribers, Blogs


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


class ListCreditCardResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = "__all__"


class ListSubscriberResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = "__all__"


class ListBlogsResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = "__all__"
