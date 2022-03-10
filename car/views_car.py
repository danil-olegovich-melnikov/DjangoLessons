import json

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from . import utils


# Create your views here.
@login_required
def car_list(request: HttpRequest) -> HttpResponse:
    name = request.GET.get('car_name', '')
    cars = utils.car_get(user=request.user, name=name)

    return render(request, 'car/cars.html', context={"cars": cars, "name": name, })


@login_required
def car_add(request: HttpRequest) -> HttpResponseRedirect:
    if request.method == "POST":
        utils.car_append(
            request.user,
            request.POST.get("name", ""),
            int(request.POST.get("speed", 0)),
            int(request.POST.get("price", 0)),
        )
    return redirect(reverse('car:car_list'))


@login_required
def car_delete(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    utils.car_delete(user=request.user, pk=pk)
    return redirect(reverse('car:car_list'))


@login_required
def car_put(request: HttpRequest) -> HttpResponseRedirect:
    if request.method == "PUT":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        utils.car_put(
            request.user,
            int(body.get("pk")),
            body.get("name", ""),
            int(body.get("max_speed", 0)),
            int(body.get("price", 0))
        )
    return redirect(reverse('car:car_list'))
