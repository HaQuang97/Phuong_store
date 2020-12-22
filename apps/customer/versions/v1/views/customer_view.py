import json

from django.db.models.query import Prefetch
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.authentication.models import User
from apps.customer.models import Contact, CreditCard
from apps.customer.versions.v1.serializers.request_serializer import AddNewContactRequestSerializer
from apps.customer.versions.v1.serializers.response_serializer import ListContactResponseSerializer, \
    ListUserResponseSerializer
from apps.utils.error_code import ErrorCode
from apps.utils.permission import IsAdminOrSubAdmin
from apps.utils.views_helper import GenericViewSet


class CustomerView:
    @method_decorator(name='list', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='create', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(auto_schema=None))
    class CustomerViewViewSet(GenericViewSet):
        queryset = User.objects.all()
        action_serializers = {
            "list_user_response": ListUserResponseSerializer,
            "list_contact_response": ListContactResponseSerializer,
            "add_new_contact_request": AddNewContactRequestSerializer,
        }

        def list(self, request, custom_queryset=None, custom_query_params=None, *args, **kwargs):
            pass

        def create(self, request, *args, **kwargs):
            pass

        def retrieve(self, request, custom_object=None, *args, **kwargs):
            pass

        def update(self, request, custom_instance=None, custom_data=None, *args, **kwargs):
            pass

        def partial_update(self, request, custom_instance=None, custom_data=None, *args, **kwargs):
            pass

        def destroy(self, request, *args, **kwargs):
            pass

        @action(detail=False, methods=['get'],
                url_path='list-contact')
        def list_contact(self, request, *args, **kwargs):
            query = Contact.objects.all()
            data = ListContactResponseSerializer(query, many=True).data
            return super().custom_response(data)

        @action(detail=False, methods=['post'],
                url_path='add-new-contact')
        def add_new_contact(self, request, *args, **kwargs):
            serializer = AddNewContactRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                Contact.objects.create(
                    full_name=serializer.validated_data['full_name'],
                    email=serializer.validated_data['email'],
                    body=serializer.validated_data['body']
                )
            return super().custom_response({"Cảm ơn bạn đã gửi tin nhắn đến cho chúng tôi.Chúng tôi sẽ liên lạc lại "
                                            "sớm nhất có thể"})
