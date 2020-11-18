import random
import re
from datetime import datetime, date

from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.authentication.models import User
from apps.utils.config import AvatarDefault
from apps.utils.error_code import ErrorCode
from apps.utils.exception import CustomException


class UserSerisalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
    
    def validate(self, attrs):
        if 'email' in attrs:
            attrs['email'] = attrs['email'].lower()
        instance = User.objects.filter(email=attrs['email'])
        if not instance.exists():
            raise Exception("Not exists email")
        return attrs


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'nickname')
        extra_kwargs = {
            'email': {'required': True},
        }
    
    def validate(self, attrs):
        if 'email' in attrs:
            attrs['email'] = attrs['email'].lower()
        instance = User.objects.filter(email=attrs['email'])
        if instance.exists():
            raise CustomException(ErrorCode.account_has_exist)
        return attrs
    
    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            username=validated_data.get('email'),
            nickname=validated_data.get('nickname'),
        )
        avatar_default = random.choice(AvatarDefault.avatar_default)
        user.avatar = avatar_default
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class AccountRequestSerializer(serializers.ModelSerializer):
    birthday = serializers.CharField(required=False)
    is_send_email = False
    
    class Meta:
        model = User
        fields = ('avatar', 'birthday', 'gender', 'introduction', 'email', 'nickname')
        extra_kwargs = {
            'avatar': {'required': False},
            'birthday': {'input_formats': settings.BIRTHDAY_FORMATS},
            'gender': {'required': False},
            'introduction': {'required': False, 'allow_null': True},
            'email': {'required': False},
            'nickname': {'required': False},
        }
    
    def validate_birthday(self, value):
        try:
            current_date = date.today()
            birthday = datetime.strptime(value, settings.BIRTHDAY_FORMATS[0])
        except:
            raise CustomException(ErrorCode.birthday_invalid_format)
        if birthday.date() > current_date:
            raise CustomException(ErrorCode.birthday_invalid_date)
        return birthday.date()


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(max_length=128)
    
    def validate(self, attrs):
        request = self.context['request']
        user = User.objects.get(id=request.user.id)
        if not user.check_password(attrs.get('old_password', None)):
            raise serializers.ValidationError('wrong password')
        if not attrs.get('new_password', None):
            raise serializers.ValidationError('new password not null')
        return attrs


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=6, required=True)
    
    def validate(self, attrs):
        email = attrs['email'].lower()
        user = authenticate(username=email, password=attrs['password'])
        if not user:
            raise CustomException(ErrorCode.login_fail)
        return user
