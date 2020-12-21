from django.urls import path, include

from apps.cms_admin.versions.v1.router import cms_admin_urlpatterns_v1

urlpatterns = [
    path('cms-admin/', include(cms_admin_urlpatterns_v1)),
]
