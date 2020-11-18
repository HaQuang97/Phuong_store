from rest_framework.routers import DefaultRouter

from apps.cms_admin.versions.v1.views import cms_admin_view

#
router = DefaultRouter()
router.register(r'v1', cms_admin_view.CmsAdminView.CmsAdminViewViewSet)
urlpatterns = router.urls
cms_admin_urlpatterns_v1 = urlpatterns
