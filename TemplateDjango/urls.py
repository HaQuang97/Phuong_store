import os

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from apps.authentication.urls import urlpatterns as auth_urlpatterns
from apps.cms_admin.urls import urlpatterns as cms_admin
from apps.customer.urls import urlpatterns as customer

schema_view = get_schema_view(
    openapi.Info(title="TemplateDjango API",
                 default_version='v1',
                 description="Document of TemplateDjango API",
                 contact=openapi.Contact(email="phuongpham98ptit@gmail.com"),
                 license=openapi.License(name="BSD License"),
                 ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_urls = [
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),
]

urlpatterns = [path('admin/', admin.site.urls)]
urlpatterns += auth_urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += cms_admin
urlpatterns += customer

env = os.environ
project_environment = env.get('ENVIRONMENT') if env.get('ENVIRONMENT') else 'development'
if settings.DEBUG:
    urlpatterns += swagger_urls

if settings.SILK_ENABLE:
    urlpatterns += [url(r'^silk/', include('silk.urls', namespace="silk"))]
