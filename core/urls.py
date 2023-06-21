from django.urls import path

from . import views


urlpatterns = [
    path("list_users/", views.list_users, name="list-users"),
]
