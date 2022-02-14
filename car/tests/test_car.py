from typing import List
from unittest import TestCase

from django.test import Client
from django.urls import reverse


URL_CAR_LIST = "/car/"
URL_CAR_ADD = "/car/add/"


CAR = {
    "name": "X",
    "price": -1,
    "speed": -1,
}


def car_count(cars: List) -> int:
    """ Find the number of the CAR in cars """
    return sum([c.name == CAR["name"] and c.price == CAR["price"] and c.speed == CAR["speed"] for c in cars])


class CarTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

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
        response = c.post(URL_CAR_ADD, CAR)
        self.assertEqual(response.url, URL_CAR_LIST)

        response = c.get(URL_CAR_LIST)
        cars = response.context['cars']

        self.assertEqual(car_count(cars), 1)