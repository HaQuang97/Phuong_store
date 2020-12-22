from rest_framework.routers import DefaultRouter

from apps.customer.versions.v1.views import customer_view

#
router = DefaultRouter()
router.register(r'v1', customer_view.CustomerView.CustomerViewViewSet)
urlpatterns = router.urls
customer_urlpatterns_v1 = urlpatterns
