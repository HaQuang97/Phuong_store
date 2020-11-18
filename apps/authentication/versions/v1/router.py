from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.authentication.versions.v1.views import auth_view
from apps.authentication.versions.v1.views import account_view
router_auth = DefaultRouter()
router_auth.register(r'v1/register', auth_view.UserCreateView.UserCreateViewSet)
router_auth.register(r'v1/logout', auth_view.LogoutView.LogoutViewSet)

auth_urlpatterns = [
    url(r'v1/login/$', auth_view.AuthenticationView.AuthenticationViewSet.as_view()),
    # url(r'v1/change-password/$', auth_view.ChangePassWordViewSet.as_view({'patch': 'partial_update'})),
]
auth_urlpatterns += router_auth.urls


router_account = DefaultRouter()
router_account.register(r'v1', account_view.AccountView.AccountViewSet)
account_urlpatterns = router_account.urls

