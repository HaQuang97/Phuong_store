import json

from django.db.models.query import Prefetch
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.authentication.models import User
from apps.cms_admin.models import Category, Items, ItemImages, Orders, OrderDetails
from apps.cms_admin.versions.v1.serializers.request_serializer import AddNewCategoryRequestSerializer, \
    UpdateCategoryRequestSerializer, DeleteCategoryRequestSerializer, AddNewItemRequestSerializer, \
    UpdateItemRequestSerializer, DeleteItemRequestSerializer, UploadImageItemRequestSerializer, \
    AddNewOrderRequestSerializer, UpdateOrderRequestSerializer
from apps.cms_admin.versions.v1.serializers.response_serializer import ListUserResponseSerializer, \
    ListCategoryResponseSerializer, ListItemResponseSerializer, ListOrderResponseSerializer
from apps.utils.error_code import ErrorCode
from apps.utils.permission import IsAdminOrSubAdmin
from apps.utils.views_helper import GenericViewSet


class CmsAdminView:
    user_id = openapi.Parameter('user_id', openapi.IN_QUERY,
                                description="ID of User",
                                type=openapi.TYPE_INTEGER, required=True)

    order_id = openapi.Parameter('order_id', openapi.IN_QUERY,
                                 description="ID of Order",
                                 type=openapi.TYPE_INTEGER, required=True)

    @method_decorator(name='list', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='create', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(auto_schema=None))
    @method_decorator(name='change_role_account', decorator=swagger_auto_schema(manual_parameters=[user_id]))
    @method_decorator(name="get_order_detail", decorator=swagger_auto_schema(manual_parameters=[order_id]))
    class CmsAdminViewViewSet(GenericViewSet):
        queryset = User.objects.all()
        action_serializers = {
            "list_user_response": ListUserResponseSerializer,
            "list_category_response": ListCategoryResponseSerializer,
            "add_new_category_request": AddNewCategoryRequestSerializer,
            "add_new_category_response": ListCategoryResponseSerializer,
            "update_category_request": UpdateCategoryRequestSerializer,
            'delete_category_request': DeleteCategoryRequestSerializer,
            "list_item_response": ListItemResponseSerializer,
            "add_new_item_request": AddNewItemRequestSerializer,
            'upload_image_item_request': UploadImageItemRequestSerializer,
            "update_item_request": UpdateItemRequestSerializer,
            "delete_item_request": DeleteItemRequestSerializer,
            "list_order_response": ListOrderResponseSerializer,
            "add_new_order_request": AddNewOrderRequestSerializer,
            "update_order_request": UpdateOrderRequestSerializer
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

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['get'],
                url_path='list-account')
        def list_account(self, request, *args, **kwargs):
            query = User.objects.all()
            data = ListUserResponseSerializer(query, many=True).data
            return super().custom_response(data)

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='change-role-account')
        def change_role_account(self, request, *args, **kwargs):
            user_id = int(request.query_params['user_id'])
            user_filter = User.objects.filter(id=user_id)
            if request.user.is_admin_user:
                user_filter.update(is_admin=True)
                data = ListUserResponseSerializer(user_filter, many=True).data
            else:
                data = {
                    'id': request.user.id,
                    'message': ErrorCode.permission,
                }
            return super().custom_response(data)

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['get'],
                url_path='list-category')
        def list_category(self, request, *args, **kwargs):
            query = Category.objects.all().order_by('-updated_at')
            data = ListCategoryResponseSerializer(query, many=True).data
            return super().custom_response(data)

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='add-new-category')
        def add_new_category(self, request, *args, **kwargs):
            serializer = AddNewCategoryRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                Category.objects.create(
                    name=serializer.validated_data['name'],
                    description=serializer.validated_data['description']
                )
            return super().custom_response({})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='update-category')
        def update_category(self, request, *args, **kwargs):
            serializer = UpdateCategoryRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                data = Category.objects.filter(id=serializer.validated_data['category_id'])
                data.update(
                    name=serializer.validated_data['name'],
                    description=serializer.validated_data['description']
                )
            return super().custom_response({})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='delete-category')
        def delete_category(self, request, *args, **kwargs):
            serializer = DeleteCategoryRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                category_id_list = serializer.data['category_id']
                queryset = Category.objects.filter(id__in=category_id_list)
                for item in queryset:
                    item.delete()
            return super().custom_response({})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['get'],
                url_path='list-item')
        def list_items(self, request, *args, **kwargs):
            query = Items.objects.all().order_by('-updated_at')
            data = ListItemResponseSerializer(query, many=True).data
            return super().custom_response(data)

        @action(detail=False, parser_classes=[MultiPartParser, ], permission_classes=[IsAdminOrSubAdmin],
                methods=['post'], url_path='upload-image-item')
        def upload_image_item(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            response = []
            if serializer.is_valid(raise_exception=True):
                content = {
                    "image": serializer.validated_data['image'],
                    "type_image": serializer.validated_data['type'],
                }
                instance = ItemImages.objects.create(**content)
                response.append({
                    "url_image": self.request.build_absolute_uri(instance.image.url),
                    "type_image": instance.type_image,
                })
            return super().custom_response(response)

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='add-new-item')
        def add_new_item(self, request, *args, **kwargs):
            serializer = AddNewItemRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                Items.objects.create(
                    category_id=serializer.validated_data['category_id'],
                    name=serializer.validated_data['name'],
                    description=serializer.validated_data['description'],
                    short_description=serializer.validated_data['short_description'],
                    image=json.dumps(serializer.validated_data['image']),
                    price_temp=serializer.validated_data['price_temp'],
                    price=serializer.validated_data['price'],
                    view_item=0
                )
            return super().custom_response({})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='update-item')
        def update_item(self, request, *args, **kwargs):
            serializer = UpdateItemRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                data = Items.objects.filter(id=serializer.validated_data['item_id'])
                data.update(
                    name=serializer.validated_data['name'],
                    description=serializer.validated_data['description'],
                    short_description=serializer.validated_data['short_description'],
                    image=json.dumps(serializer.validated_data['image']),
                    price_temp=serializer.validated_data['price_temp'],
                    price=serializer.validated_data['price'],
                    view_item=0
                )
            return super().custom_response({})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['post'],
                url_path='delete-item')
        def delete_item(self, request, *args, **kwargs):
            serializer = DeleteItemRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                item_id_list = serializer.data['item_id']
                queryset = Items.objects.filter(id__in=item_id_list)
                for item in queryset:
                    item.delete()
            return super().custom_response({})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['get'],
                url_path='list-order')
        def list_order(self, request, *args, **kwargs):
            query = Orders.objects.all().order_by('-updated_at')
            data = ListOrderResponseSerializer(query, many=True).data
            return super().custom_response(data)

        @action(detail=False, permission_classes=[IsAuthenticated], methods=['post'],
                url_path='add-new-order')
        def add_new_order(self, request, *args, **kwargs):
            serializer = AddNewOrderRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                item_filter = Items.objects.filter(id=serializer.data['item_id']).get()
                instance = Orders.objects.create(
                    name=request.user.full_name,
                    phone=request.user.phone,
                    address=request.user.address,
                    user_id=request.user.id,
                )
                order_detail = OrderDetails.objects.create(
                    quantity=serializer.data['quantity'],
                    unit_price=item_filter.price,
                    total_price=serializer.data['quantity'] * item_filter.price,
                    item_id=item_filter.id,
                    order=instance
                )
            return super().custom_response({})

        @action(detail=False, permission_classes=[IsAuthenticated], methods=['post'],
                url_path='update-order')
        def update_order(self, request, *args, **kwargs):
            serializer = UpdateOrderRequestSerializer(data=request.data, context=self.get_serializer_context())
            if serializer.is_valid(raise_exception=True):
                order_filter = Orders.objects.filter(id=serializer.data['order_id'])
                instance = order_filter.update(
                    status=serializer.data['status']
                )
            return super().custom_response({})

        @action(detail=False, permission_classes=[IsAdminOrSubAdmin], methods=['get'],
                url_path='get-order-detail')
        def get_order_detail(self, request, *args, **kwargs):
            order_id = int(request.query_params['order_id'])
            order_filter = OrderDetails.objects.filter(order_id=order_id).prefetch_related(
                Prefetch(
                    'order',
                    queryset=Orders.objects.filter(id=order_id),
                    to_attr='order_data'
                )
            ).get()
            item = {
                "name": order_filter.item.name,
                "description": order_filter.item.description,
                "price": order_filter.item.price,
                "image": json.loads(order_filter.item.image)
            }
            user_data = {
                "name": order_filter.order_data.user.full_name,
                "address": order_filter.order_data.user.address,
                "phone": order_filter.order_data.user.phone
            }
            detail = {
                "customer": user_data,
                "item": item,
                "quantity": order_filter.quantyti,
                "total_price": order_filter.total_price
            }
            return super().custom_response(detail)
