import json

from django.db.models.query import Prefetch
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.authentication.models import User
from apps.customer.models import Contact, CreditCard, Blogs, Subscribers
from apps.customer.versions.v1.serializers.request_serializer import AddNewContactRequestSerializer, \
    DeleteBlogsRequestSerializer, DeleteSubscriberRequestSerializer, AddBlogsRequestSerializer, \
    AddSubscriberRequestSerializer, AddCreditCardRequestSerializer, DeleteCreditCardRequestSerializer, \
    DeleteContactRequestSerializer, UpdateBlogsRequestSerializer

from apps.customer.versions.v1.serializers.response_serializer import ListContactResponseSerializer, \
    ListUserResponseSerializer, ListBlogsResponseSerializer, ListSubscriberResponseSerializer, \
    ListCreditCardResponseSerializer
from apps.utils.error_code import ErrorCode
from apps.utils.permission import IsAdminOrSubAdmin
from apps.utils.views_helper import GenericViewSet


class CustomerView:
    user_id = openapi.Parameter('user_id', openapi.IN_QUERY,
                                description="ID of User",
                                type=openapi.TYPE_INTEGER, required=True)
    contact_id = openapi.Parameter('order_id', openapi.IN_QUERY,
                                   description="ID of Contact",
                                   type=openapi.TYPE_INTEGER, required=True)
    credit_card_id = openapi.Parameter('order_id', openapi.IN_QUERY,
                                       description="ID of Credit Card",
                                       type=openapi.TYPE_INTEGER, required=True)
    blog_id = openapi.Parameter('order_id', openapi.IN_QUERY,
                                description="ID of Blog",
                                type=openapi.TYPE_INTEGER, required=True)
    subscriber_id = openapi.Parameter('order_id', openapi.IN_QUERY,
                                      description="ID of Subscriber",
                                      type=openapi.TYPE_INTEGER, required=True)

    @method_decorator(name='list', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='create', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name="get_blog_detail", decorator=swagger_auto_schema(manual_parameters=[blog_id]))
    class CustomerViewViewSet(GenericViewSet):
        queryset = User.objects.all()
        action_serializers = {
            "list_user_response": ListUserResponseSerializer,
            "list_contact_response": ListContactResponseSerializer,
            "list_credit_card_response": ListCreditCardResponseSerializer,
            "list_blog_response": ListBlogsResponseSerializer,
            "list_subscriber_response": ListSubscriberResponseSerializer,
            "add_new_contact_request": AddNewContactRequestSerializer,
            "add_new_credit_card_request": AddCreditCardRequestSerializer,
            "add_new_blog_request": AddBlogsRequestSerializer,
            "add_new_subscriber_request": AddSubscriberRequestSerializer,
            "update_blog_request": UpdateBlogsRequestSerializer,
            "delete_contact_request": DeleteContactRequestSerializer,
            "delete_credit_card_request": DeleteCreditCardRequestSerializer,
            "delete_blog_request": DeleteBlogsRequestSerializer,
            "delete_subscriber_request": DeleteSubscriberRequestSerializer,

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

        @action(detail=False, methods=['get'], permission_classes=[IsAdminOrSubAdmin],
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

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='delete-contact')
        def delete_contact(self, request, *args, **kwargs):
            serializer = DeleteContactRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                contact_id_list = serializer.data['contact_id']
                queryset = Contact.objects.filter(id__in=contact_id_list)
                for item in queryset:
                    item.delete()
            return super().custom_response({})

        @action(detail=False, permission_classes=[IsAuthenticated], methods=['post'],
                url_path='add_new_credit_card')
        def add_new_credit_card(self, request, *args, **kwargs):
            serializer = AddCreditCardRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                CreditCard.objects.create(
                    full_name=serializer.validated_data['full_name'],
                    number_credit=serializer.validated_data['number_credit'],
                    expire_date=serializer.validated_data['expire_date'],
                    CVV=serializer.validated_data['CVV'],
                    address=serializer.validated_data['address']
                )
            return super().custom_response({"OK"})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='delete-credit-card')
        def delete_credit_card(self, request, *args, **kwargs):
            serializer = DeleteCreditCardRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                credit_card_id_list = serializer.data['credit_card_id']
                queryset = CreditCard.objects.filter(id__in=credit_card_id_list)
                for item in queryset:
                    item.delete()
            return super().custom_response({"OK"})

        @action(detail=False, methods=['post'],
                url_path='add_new_subscriber')
        def add_new_subscriber(self, request, *args, **kwargs):
            serializer = AddSubscriberRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                Subscribers.objects.create(
                    email=serializer.validated_data['email'],
                )
            return super().custom_response({"OK"})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='delete-subscriber')
        def delete_subscriber(self, request, *args, **kwargs):
            serializer = DeleteSubscriberRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                subscriber_id_list = serializer.data['subscriber_id']
                queryset = Subscribers.objects.filter(id__in=subscriber_id_list)
                for item in queryset:
                    item.delete()
            return super().custom_response({"OK"})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['get'],
                url_path='get_blog_detail')
        def get_blog_detail(self, request, *args, **kwargs):
            blog_id = int(request.query_params['blog_id'])
            query = Blogs.objects.filter(blog_id=blog_id).order_by('-updated_at')
            data = ListBlogsResponseSerializer(query, many=True).data
            return super().custom_response(data)

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='add_new_blog')
        def add_new_blog(self, request, *args, **kwargs):
            serializer = AddBlogsRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                Blogs.objects.create(
                    title=serializer.validated_data["title"],
                    description=serializer.validated_data["description"],
                    author=serializer.validated_data["author"],
                    image=serializer.validated_data["image"],
                    like=serializer.validated_data["like"],
                )
            return super().custom_response({"OK"})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='update_blog')
        def update_blog(self, request, *args, **kwargs):
            serializer = UpdateBlogsRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                data = Blogs.objects.filter(id=serializer.validated_data['supplier_id'])
                data.update(
                    title=serializer.validated_data["title"],
                    description=serializer.validated_data["description"],
                    author=serializer.validated_data["author"],
                    image=serializer.validated_data["image"],
                    like=serializer.validated_data["like"],
                )
            return super().custom_response({"Success"})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='delete-blog')
        def delete_blog(self, request, *args, **kwargs):
            serializer = DeleteBlogsRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                blog_id_list = serializer.data['blog_id']
                queryset = Blogs.objects.filter(id__in=blog_id_list)
                for item in queryset:
                    item.delete()
            return super().custom_response({"Success"})
