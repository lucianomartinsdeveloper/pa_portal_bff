from django.contrib import admin
from django.urls import path, include

from .api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('client.urls', namespace='client')),
    path('api/v2/', api.urls),
]
