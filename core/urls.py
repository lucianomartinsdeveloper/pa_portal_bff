from django.urls import path

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("list_users")

urlpatterns = [
    path("list_users/", router.urls),
]
