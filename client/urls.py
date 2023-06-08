from django.urls import include, path
from rest_framework import routers

from api_drf.viewsets import ClientViewSet

app_name = 'client'

router = routers.DefaultRouter()

router.register(r'clients', ClientViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
