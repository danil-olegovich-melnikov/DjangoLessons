from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from . import models


def register(request: HttpRequest) -> HttpResponse:
    context = {"message": "", "username": "", "user": request.user}
    if request.method == "POST":
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")

        error = ""
        if username == "":
            error = "Введите имя пользователя"
        elif email == "":
            error = "Введите почту пользователя"
        elif User.objects.filter(email=email).count() > 0:
            user = User.objects.get(email=email)
            if user.is_active:
                link = f"<a href='{reverse('worker:login')}'>Войти в аккаунт</a>"
            else:
                link = f"<br>Нужно <a href='{reverse('worker:verification')}'>активировать аккаунт</a>"

            error = f"Данная почта уже используется {link}"
        elif password1 == "":
            error = "Введите пароль"
        elif password1 != password2:
            error = "Пароли не совпадают"
        elif User.objects.filter(username=username).count() > 0:
            error = f"Данный никнейм уже занят <a href='{reverse('worker:verification')}>Активировать аккаунт</a>'>"

        if error == "":
            user = User.objects.create_user(username=username, password=password1)
            user.email = email
            user.is_active = False
            user.save()
            models.EmailCode(user=user).save()
            return redirect(reverse("worker:verification"))

        context["username"] = request.POST.get("username", "")
        context["message"] = error

    return render(request, "registration/register.html", context=context)


def email_verification(request):
    if request.method == "POST":
        email = request.POST.get("email")
        code = request.POST.get("code")

        user = User.objects.filter(email=email)

        if not user.exists():
            return redirect(request.path_info)

        user = user[0]

        if user.is_active:
            return redirect(request.path_info)

        email_code = models.EmailCode.objects.filter(user=user, code=code)
        if not email_code.exists():
            models.EmailCode.objects.get(user=user).save()

        user.is_active = True
        user.save()

    return render(request, 'registration/verification.html', context={})