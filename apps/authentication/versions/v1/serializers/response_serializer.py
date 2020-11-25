from datetime import date

from django.conf import settings
from rest_framework import serializers

from apps.authentication.models import User


class AccountResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'birthday': {'format': settings.BIRTHDAY_FORMATS[0]},
            'created_at': {'format': settings.DATE_TIME_FORMATS[0]},
        }


class AccountDetailSerializer(AccountResponseSerializer):
    age = serializers.SerializerMethodField()
    is_new_user = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'birthday': {'format': settings.BIRTHDAY_FORMATS[0]},
            'created_at': {'format': settings.DATE_TIME_FORMATS[0]},
        }
    
    def get_is_new_user(self, obj):
        context = self.context
        if 'is_new_user' in context:
            return context['is_new_user']
        return False
    
    def get_age(self, obj):
        if obj.birthday:
            today = date.today()
            age = today.year - obj.birthday.year - ((today.month, today.day) < (obj.birthday.month, obj.birthday.day))
            return age
        return None


class UserProfileSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'format': settings.DATE_TIME_FORMATS[0]},
        }
    
    def get_age(self, obj):
        if obj.birthday:
            today = date.today()
            age = today.year - obj.birthday.year - ((today.month, today.day) < (obj.birthday.month, obj.birthday.day))
            return age
        return None
