from django.urls import path

from rest_framework.routers import SimpleRouter

from core.views import UsersViewSets


# router = DefaultRouter()
router = SimpleRouter()
router.register("list_users", UsersViewSets)

urlpatterns = router.urls
