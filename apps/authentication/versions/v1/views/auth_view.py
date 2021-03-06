# import random
# import random
# import tempfile
from datetime import datetime, timedelta

# import jwt
# import requests
# from django.conf import settings
# from django.core.exceptions import ObjectDoesNotExist
# from django.core.files import File
# from django.utils import timezone
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_jwt.views import JSONWebTokenAPIView

import apps.utils.response_interface as rsp
from apps.authentication.models import User, Token
from apps.authentication.utils.custom_auth import JWTToken
from apps.authentication.utils.send_mail import EmailTemplate
from apps.authentication.versions.v1.serializers.request_serializer import LoginSerializer, UserCreateSerializer, \
    ChangePasswordSerializer, CheckEmailSerializer, CheckOTPCodeSerializer, ForgotPasswordSerializer
from apps.authentication.versions.v1.serializers.response_serializer import UserSerializer, UserResponseSerializer
from apps.utils import send_email
from apps.utils.error_code import ErrorCode
from apps.utils.exception import CustomException
from apps.utils.views_helper import GenericViewSet, EmptySerializer


class AuthenticationView:
    class AuthenticationViewSet(JSONWebTokenAPIView):
        serializer_class = LoginSerializer

        def post(self, request, *args, **kwargs):

            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.validated_data
                time_token = int(datetime.timestamp(datetime.utcnow()))
                Token.objects.create(user=user, token=time_token)
                return JWTToken(user, time_token).make_token(user, status=status.HTTP_200_OK)
            else:
                raise AuthenticationFailed


class UserCreateView:
    @method_decorator(name='list', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(auto_schema=None))
    class UserCreateViewSet(GenericViewSet):
        serializer_class = UserCreateSerializer
        queryset = User.objects.all()

        def list(self, request, custom_queryset=None, custom_query_params=None, *args, **kwargs):
            pass

        def retrieve(self, request, custom_object=None, *args, **kwargs):
            pass

        def destroy(self, request, *args, **kwargs):
            pass

        def update(self, request, custom_instance=None, custom_data=None, *args, **kwargs):
            pass

        def partial_update(self, request, custom_instance=None, custom_data=None, *args, **kwargs):
            pass

        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            time_token = int(datetime.timestamp(datetime.utcnow()))
            instance = self.perform_create(serializer)

            # todo send email here
            # send_email()
            # send activation email to user
            mail_template = EmailTemplate()
            mail_template.send_activation_email(instance)

            Token.objects.create(user=instance, token=time_token)
            token = JWTToken(instance, time_token, True).make_token(request, status=status.HTTP_201_CREATED)
            return token


class LogoutView:
    @method_decorator(name='list', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(auto_schema=None))
    class LogoutViewSet(GenericViewSet):
        serializer_class = EmptySerializer
        queryset = User.objects.all()
        permission_classes = (IsAuthenticated,)

        def create(self, request, *args, **kwargs):
            Token.objects.filter(user=request.user, token=request.auth.token).delete()
            general_response = rsp.Response(None).generate_response()
            return Response(general_response, status=status.HTTP_200_OK)


class ChangePassWordViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        obj = self.request.user
        return obj

    def partial_update(self, request, custom_instance=None, custom_data=None, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            obj.set_password(serializer.data.get('new_password'))
            obj.save()
            general_response = rsp.Response(None).generate_response()
            return Response(general_response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyAccountView:
    @method_decorator(name='list', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='create', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(auto_schema=None))
    class VerifyAccountViewSet(GenericViewSet):
        serializer_class = CheckEmailSerializer
        queryset = User.objects.all()
        action_serializers = {
            'check_exist_email_request': CheckEmailSerializer,
            'check_auth_code_request': CheckOTPCodeSerializer,
            'profile_response': UserSerializer,
            'send_link_forgot_password_request': ForgotPasswordSerializer,
            'read_notification_request': EmptySerializer,
        }

        def list(self, request, custom_queryset=None, custom_query_params=None, *args, **kwargs):
            pass

        def retrieve(self, request, custom_object=None, *args, **kwargs):
            pass

        def destroy(self, request, *args, **kwargs):
            try:
                instance = User.objects.get(pk=kwargs.get('pk', None))
                self.perform_destroy(instance)
                general_response = rsp.Response(None).generate_response()
                return Response(general_response, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                raise CustomException(ErrorCode.not_found_record)

        def update(self, request, custom_instance=None, custom_data=None, *args, **kwargs):
            pass

        def partial_update(self, request, custom_instance=None, custom_data=None, *args, **kwargs):
            pass

        def create(self, request, *args, **kwargs):
            pass

        @action(detail=False, methods=['post'], url_path='check-exist-email')
        def check_exist_email(self, request, *args, **kwargs):
            serializer = CheckEmailSerializer(data=request.data, **kwargs)
            if serializer.is_valid(raise_exception=True):
                data = serializer.validated_data
                general_response = rsp.Response(data).generate_response()
                return Response(general_response, status=status.HTTP_200_OK)

        @action(detail=False, methods=['post'], url_path='check-auth-code')
        def check_auth_code(self, request, *args, **kwargs):
            serializer = CheckOTPCodeSerializer(data=request.data, **kwargs)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()

                time_token = int(datetime.timestamp(datetime.utcnow()))
                Token.objects.create(user=user, token=time_token)
                return JWTToken(user, time_token).make_token(user, status=status.HTTP_200_OK)

        @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated], url_path='profile')
        def profile(self, request, *args, **kwargs):
            data = UserSerializer(request.user).data
            return super().custom_response(data)

        @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='send-link-forgot-password')
        def send_link_forgot_password(self, request, *args, **kwargs):
            user = self.get_users(request.data.get('email'))
            mail_template = EmailTemplate()
            mail_template.send_forgot_password_email(user)
            return super().custom_response(UserResponseSerializer(user).data)

        def get_users(self, email):
            try:
                return User.objects.get(email__iexact=email)
            except User.DoesNotExist:
                raise CustomException(ErrorCode.wrong_email)
