# Create your views here.
import datetime
from datetime import date

from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import apps.utils.response_interface as rsp
from apps.authentication.models import User
from apps.authentication.versions.v1.serializers.request_serializer import AccountRequestSerializer
from apps.authentication.versions.v1.serializers.response_serializer import AccountDetailSerializer, \
    AccountResponseSerializer, UserProfileSerializer
from apps.utils.error_code import ErrorCode
from apps.utils.exception import CustomException
from apps.utils.views_helper import GenericViewSet


class AccountView:
    user_id = openapi.Parameter(
        'user_id',
        openapi.IN_QUERY,
        description="Use get user profile",
        type=openapi.TYPE_INTEGER,
        required=True
    )
    
    @method_decorator(name='create', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(auto_schema=None))
    class AccountViewSet(GenericViewSet):
        permission_classes = [IsAuthenticated]
        action_serializers = {
            'list_response': AccountDetailSerializer,
            'update_profile_request': AccountRequestSerializer,
            'update_profile_response': AccountResponseSerializer,
            'user_profile_response': UserProfileSerializer
        }
        queryset = User.objects.all()
        parser_classes = [JSONParser]
        
        def list(self, request, *args, **kwargs):
            context = {"request": request}
            user_profile = User.objects.get(pk=request.user.id)
            serializer = AccountDetailSerializer(user_profile, context=context)
            general_response = rsp.Response(serializer.data).generate_response()
            return Response(general_response, status=status.HTTP_200_OK)
        
        @action(detail=False, methods=['patch'], url_path='update-profile')
        def update_profile(self, request, *args, **kwargs):
            kwargs['partial'] = True
            return super().update(request, custom_instance=request.user, *args, **kwargs)
        
        @action(detail=False, methods=['get'], url_path='user-profile')
        def user_profile(self, request, *args, **kwargs):
            try:
                user_id = request.query_params.get('user_id', None)
                user_profile = User.objects.filter(pk=user_id).first()
                data = UserProfileSerializer(user_profile).data
                general_response = rsp.Response(data).generate_response()
                return Response(general_response, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                raise CustomException(ErrorCode.not_found_record)
        
        def get_users(self, email):
            try:
                return User.objects.get(email__iexact=email)
            except ObjectDoesNotExist:
                raise CustomException(ErrorCode.wrong_email)
