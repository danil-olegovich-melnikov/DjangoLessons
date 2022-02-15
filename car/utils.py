from typing import List

from . import models
from .db import *

if 'cars' not in globals():
    cars = []


def get() -> List:
    """ Retrieve all the car instances from db"""
    return models.Car.objects.all()


def put(pk: int, name: str, speed: int, price: int) -> None:
    """ Replace the car instance by pk """
    instance = models.Car.objects.filter(id=pk)
    if instance.exists():
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
