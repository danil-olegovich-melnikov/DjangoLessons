from typing import List

from django.core.paginator import Paginator

from . import models


def car_get(name: str) -> List[models.Car]:
    """ Retrieve all the car instances from db"""
    cars = models.Car.objects.all()

    if len(name) > 0:
        cars = cars.filter(name__icontains=name)

    return cars


def car_get_by_pk(pk) -> models.Car:
    """ Retrieve all the car instances from db"""
    return models.Car.objects.get(pk=pk)


def car_put(pk: int, name: str, speed: int, price: int) -> None:
    """ Replace the car instance by pk """
    instance = models.Car.objects.filter(id=pk)

    if not instance.exists():
        return

    instance = instance[0]
    instance.name = name
    instance.speed = speed
    instance.price = price
    instance.save()


def car_delete(pk: int) -> None:
    """ Delete the car instance by pk """
    models.Car.objects.filter(id=pk).delete()


def car_append(name: str, speed: int, price: int) -> None:
    """ Append the car instance """
    models.Car(name=name, speed=speed, price=price).save()


def trip_get(pk: int, start_day: str, end_day: str) -> Paginator:
    """ Get the trip instances by car id """
    cars = models.Trip.objects.all()

    if pk > -1:
        cars = cars.filter(car=pk)
    if len(start_day) > 0:
        cars = cars.filter(date__gte=start_day)
    if len(end_day) > 0:
        cars = cars.filter(date__lte=end_day)

    return Paginator(cars, 5)


def trip_append(pk: int, number_of_km: int, date: str) -> None:
    """ Append the trip instance """
    car = models.Car.objects.get(id=pk)
    trip = models.Trip(car=car, number_of_km=number_of_km)

    if len(date) > 0:
        trip.date = date

    trip.save()


def trip_delete(pk: int) -> None:
    """ Delete the car instance by pk """
    models.Trip.objects.filter(id=pk).delete()
