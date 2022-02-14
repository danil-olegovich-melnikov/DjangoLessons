from .db import *


if 'cars' not in globals():
    cars = []

def put(pk: int, name: str, speed: int, price: int) -> None:
    """ Replace the car instance by pk """

    car_index = -1
    for index, car in enumerate(cars):
        if car.id == pk:
            car_index = index
            break

    if car_index == -1:
        return

    cars[car_index] = Car(pk, name, speed, price)

def car_delete(pk: int) -> None:
    """ Delete the car instance by pk """

    global cars
    cars = [car for car in cars if car.id != pk]


def car_append(name: str, speed: int, price: int) -> None:
    """ Append the car instance """

    if len(cars):
        pk = cars[-1].id + 1
    else:
        pk = 1

    cars.append(Car(id=pk, name=name, speed=speed, price=price))

