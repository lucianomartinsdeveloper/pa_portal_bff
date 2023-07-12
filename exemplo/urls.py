from django.urls import path

from . import views


app_name = "exemplo"

urlpatterns = [
    path("", views.index, name="index"),
    path("logar/", views.logar, name="logar"),
    path("sair/", views.sair, name="sair"),
    path("list_users/", views.list_users, name="list_users"),
]
