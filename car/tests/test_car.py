from typing import List
from unittest import TestCase

from django.test import Client
from django.urls import reverse

from car.utils import car_append
from car.utils import car_delete

from car.db import Car

URL_CAR_LIST = "/car/"
URL_CAR_ADD = "/car/add/"
URL_CAR_PUT = "/car/delete/"


CAR1 = {
    "name": "X",
    "price": -1,
    "speed": -1,
}

CAR2 = {
    "name": "N",
    "price": -1,
    "speed": -1,
}

def check_dict_class(c: dict, C: Car):
    return C.name == c["name"] and C.price == c["price"] and C.speed == c["speed"]

def car_count(cars: List, car) -> int:
    """ Find the number of the CAR in cars """
    return sum([check_dict_class(car, c) for c in cars])


class CarTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method.
        c = Client()
        self.assertEqual(reverse("car:car_list"), URL_CAR_LIST)

        response = c.get(URL_CAR_LIST)
        self.assertNotIn("cars", response.context['cars'])

        cars = response.context['cars']
        for car in cars:
            car_delete(car.id)

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_add_car(self):
        """ Test add car view """
        c = Client()
        self.assertEqual(reverse("car:car_list"), URL_CAR_LIST)

        response = c.get(URL_CAR_LIST)
        self.assertNotIn("cars", response.context['cars'])

        car_length = len(response.context['cars'])

        self.assertNotIn("cars", response.context['cars'])

        self.assertEqual(reverse("car:car_add"), URL_CAR_ADD)
        response = c.post(URL_CAR_ADD, CAR1)
        self.assertEqual(response.url, URL_CAR_LIST)

        response = c.get(URL_CAR_LIST)
        cars = response.context['cars']

        self.assertEqual(car_length + 1, len(cars))
        self.assertEqual(car_count(cars, CAR1), 1)

    def test_delete_car(self):
        c = Client()

        self.assertEqual(reverse("car:car_add"), URL_CAR_ADD)
        response = c.post(URL_CAR_ADD, CAR2)
        self.assertEqual(response.url, URL_CAR_LIST)

        response = c.get(URL_CAR_LIST)
        self.assertNotIn("cars", response.context['cars'])
        cars = response.context['cars']
        car_length = len(response.context["cars"])

        car_id = -1
        for car in cars:
            if check_dict_class(CAR2, car):
                car_id = car.id

        self.assertNotEqual(car_id, -1)
        c.get(reverse("car:car_delete", kwargs={'pk': car_id}))
        response = c.get(URL_CAR_LIST)
        cars = response.context['cars']

        self.assertEqual(car_length - 1, len(cars))
        self.assertEqual(car_count(cars, CAR2), 0)

    def test_add_car_empty_db(self):
        """ Test add car view to empty db"""
        car_append(**CAR1)

    def test_put_car(self):
        c = Client()
        self.assertEqual(reverse("car:car_add"), URL_CAR_ADD)
        response = c.post(URL_CAR_ADD, CAR2)
        self.assertEqual(response.url, URL_CAR_LIST)

        response = c.get(URL_CAR_LIST)
        self.assertNotIn("cars", response.context['cars'])
        cars = response.context['cars']

        car_id = -1
        for car in cars:
            if check_dict_class(CAR2, car):
                car_id = car.id

        car = {**CAR1, "pk": car_id}
        c.post(reverse("car:car_put"), car)
        response = c.get(URL_CAR_LIST)
        self.assertNotIn("cars", response.context['cars'])
        cars = response.context['cars']

        for car in cars:
            if car.id == car_id:
                assert check_dict_class(CAR1, car)
                break