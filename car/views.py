from collections import namedtuple
from random import randint
from typing import List

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

Car = namedtuple('Car', ['id', 'name', 'price', 'speed'])

cars: List[Car] = [
    Car(1, 'Audi', randint(1, 100) * 100000, 300),
    Car(2, 'BWM', randint(1, 100) * 100000, 320),
    Car(3, 'Mercedes', randint(1, 100) * 100000, 340),
    Car(4, 'Lada', randint(1, 100), 30),
]


def delete(pk):
    global cars
    cars = [car for car in cars if car.id != pk]


# Create your views here.
def car_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'car/index.html', context={"cars": cars})


def car_delete(request: HttpRequest, pk) -> HttpResponse:
    delete(pk)
    return redirect(reverse('car:car_list'))


def car_add(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        cars.append(
            Car(
                id=cars[-1].id + 1,
                name=request.POST.get("name", ""),
                speed=request.POST.get("speed", ""),
                price=request.POST.get("price", ""),
            )
        )
    return redirect(reverse('car:car_list'))
