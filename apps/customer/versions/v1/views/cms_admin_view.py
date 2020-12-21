import json

from django.db.models.query import Prefetch
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.authentication.models import User
from apps.cms_admin.models import Category, Items, ItemImages, Orders, OrderDetails, Supplier, Comments
from apps.cms_admin.versions.v1.serializers.request_serializer import AddNewCategoryRequestSerializer, \
    UpdateCategoryRequestSerializer, DeleteCategoryRequestSerializer, AddNewItemRequestSerializer, \
    UpdateItemRequestSerializer, DeleteItemRequestSerializer, UploadImageItemRequestSerializer, \
    AddNewOrderRequestSerializer, UpdateOrderRequestSerializer, AddNewSupplierRequestSerializer, \
    DeleteSupplierRequestSerializer, UpdateSupplierRequestSerializer, UpdateQuantityRequestSerializer, \
    DeleteCommentRequestSerializer, UpdateCommentRequestSerializer, AddNewCommentRequestSerializer
from apps.cms_admin.versions.v1.serializers.response_serializer import ListUserResponseSerializer, \
    ListCategoryResponseSerializer, ListItemResponseSerializer, ListOrderResponseSerializer, \
    ListSupplierResponseSerializer, ListCommentResponseSerializer
from apps.utils.error_code import ErrorCode
from apps.utils.permission import IsAdminOrSubAdmin
from apps.utils.views_helper import GenericViewSet


# class CustomerView: