import random
import re
from datetime import datetime, date, timezone

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.authentication.models import User, UserAuth
from apps.utils.config import PasswordRegex
from apps.utils.error_code import ErrorCode
from apps.utils.exception import CustomException
from apps.utils.constants import AuthType

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
    password = serializers.CharField(required=True, max_length=255)
    email = serializers.EmailField(required=True, max_length=255)
    birthday = serializers.CharField(required=True, max_length=255)

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name', 'phone', 'address', 'gender', 'birthday')

    def validate(self, attrs):
        if 'email' in attrs:
            attrs['email'] = attrs['email'].lower()
        instance = User.objects.filter(email=attrs['email'])
        if instance.exists():
            raise CustomException(ErrorCode.account_has_exist)
        return attrs

    def validate_birthday(self, value):
        try:
            current_date = date.today()
            birthday_user = datetime.strptime(value, settings.DATE_FORMATS[1])
        except Exception as e:
            raise CustomException(ErrorCode.birthday_invalid_format)
        if birthday_user.date() > current_date:
            raise CustomException(ErrorCode.birthday_invalid_date)
        return birthday_user.date()

    def validate_password(self, value):
        if not re.search(PasswordRegex.password_regex, value):
            raise CustomException(ErrorCode.password_invalid)
        return value

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            username=validated_data.get('email'),
            password=validated_data.get('password'),
            full_name=validated_data.get('full_name'),
            phone=validated_data.get('phone'),
            address=validated_data.get('address'),
            gender=validated_data.get('gender'),
            birthday=validated_data.get('birthday'),
            is_active=True
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class AccountRequestSerializer(serializers.ModelSerializer):
    birthday = serializers.CharField(required=False)
    is_send_email = False

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'birthday': {'input_formats': settings.BIRTHDAY_FORMATS},
            'gender': {'required': False},
            'email': {'required': False},
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
        user = authenticate(email=attrs['email'], password=attrs['password'])
        if not user:
            raise CustomException(ErrorCode.login_fail)
        return user

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class CheckEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=255)

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            return {'exist': True}
        return {'exist': False}

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class CheckOTPCodeSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=True)
    otp_code = serializers.CharField(max_length=6, required=True)

    def validate(self, attrs):
        try:
            user_code = UserAuth.objects.filter(
                user_id=attrs['user'],
                auth_code=attrs['otp_code'],
                auth_type=AuthType.ACTIVATION.value
            ).get()
            # check time code
            if not user_code.created_at >= timezone.now() - relativedelta(minutes=OTPCode.timeout_auth_code):
                raise CustomException(ErrorCode.otp_code_has_expired)
            return user_code.user
        except UserAuth.DoesNotExist:
            raise CustomException(ErrorCode.wrong_data)

    def save(self, **kwargs):
        user = self.validated_data
        user.is_active = True
        user.save()
        # delete otp code
        UserAuth.objects.filter(user=user, auth_type=AuthType.ACTIVATION.value).delete()
        return user


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, required=True)
