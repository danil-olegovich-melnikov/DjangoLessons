from django.http import HttpRequest, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from . import utils


# Create your views here.
def car_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'car/index.html', context={"cars": utils.cars})


def car_delete(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    utils.delete(pk)
    return redirect(reverse('car:car_list'))


def car_add(request: HttpRequest) -> HttpResponseRedirect:
    if request.method == "POST":
        utils.append(
            request.POST.get("name", ""),
            int(request.POST.get("speed", -1)),
            int(request.POST.get("price", -1)),
        )
    return redirect(reverse('car:car_list'))


def car_put(request: HttpRequest) -> HttpResponseRedirect:
    if request.method == "POST":
        utils.put(
            int(request.POST.get("pk", -1)),
            request.POST.get("name", ""),
            int(request.POST.get("speed", -1)),
            int(request.POST.get("price", -1))
            )
    return redirect(reverse('car:car_list'))
