from django.urls import path, include

from apps.customer.versions.v1.router import customer_urlpatterns_v1

urlpatterns = [
    path('customer/', include(customer_urlpatterns_v1)),
]
