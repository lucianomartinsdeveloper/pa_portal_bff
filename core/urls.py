from rest_framework.routers import SimpleRouter

from core.views import UsersViewSets


router = SimpleRouter()
router.register("list_users", UsersViewSets)

urlpatterns = router.urls
