from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # path("accounts/", ),
    path("admin/", admin.site.urls),
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.authtoken")),
]
