import random
import random
import tempfile
from datetime import datetime, timedelta

import jwt
import requests
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.utils import timezone
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.views import JSONWebTokenAPIView

import apps.utils.response_interface as rsp
from apps.authentication.models import User, Token
from apps.authentication.utils.custom_auth import JWTToken
from apps.authentication.versions.v1.serializers.request_serializer import LoginSerializer, UserCreateSerializer, \
    ChangePasswordSerializer
from apps.utils.views_helper import GenericViewSet, EmptySerializer


class AuthenticationView:
    class AuthenticationViewSet(JSONWebTokenAPIView):
        serializer_class = LoginSerializer
        
        def post(self, request, *args, **kwargs):
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.validated_data
                time_token = int(datetime.timestamp(datetime.utcnow()))
                Token.objects.create(user=user, token=time_token)
                token = JWTToken(user, time_token).make_token(request, status=status.HTTP_200_OK)
                return token
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
        
        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            time_token = int(datetime.timestamp(datetime.utcnow()))
            instance = self.perform_create(serializer)
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
