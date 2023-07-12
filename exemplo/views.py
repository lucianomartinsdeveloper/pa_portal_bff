from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, resolve_url

from core.models import User


def index(request):
    template_name = "exemplo/index.html"
    print(request.user.is_authenticated)
    return render(request, template_name)


def list_users(request):
    template_name = "exemplo/tabela.html"
    users = User.objects.all()
    context = {"users": users}
    return render(request, template_name, context)


def logar(request):
    template_name = "exemplo/login.html"
    msg = ""
    if request.method == "get":
        return render(request, template_name)
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is None:
            msg = "Email/senha ."
            context = {"msg": msg}
            return render(request, template_name, context)
        else:
            login(request, user)
            return redirect(resolve_url("exemplo:index"))


def sair(request):
    logout(request)
    return redirect(resolve_url("exemplo:index"))
