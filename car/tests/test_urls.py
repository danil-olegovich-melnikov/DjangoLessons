from django.test import TestCase
from django.urls import reverse, resolve
from car import views_trip, views_car


class TestUrls(TestCase):

    def test_car_list_url_resolve(self):
        url = reverse('car:car_list')
        self.assertEqual(resolve(url).func, views_car.car_list)

    def test_car_delete_url_resolve(self):
        url = reverse('car:car_delete', args=[0])
        self.assertEqual(resolve(url).func, views_car.car_delete)

    def test_car_add_url_resolve(self):
        url = reverse('car:car_add')
        self.assertEqual(resolve(url).func, views_car.car_add)

    def test_car_put_url_resolve(self):
        url = reverse('car:car_put')
        self.assertEqual(resolve(url).func, views_car.car_put)

    def test_trips_list_url_resolve(self):
        url = reverse('car:trip_list', args=[0])
        self.assertEqual(resolve(url).func, views_trip.trip_list)

    def test_trip_add_url_resolve(self):
        url = reverse('car:trip_add', args=[0])
        self.assertEqual(resolve(url).func, views_trip.trip_add)

    def test_trip_delete_url_resolve(self):
        url = reverse('car:trip_delete', args=[0, 0])
        self.assertEqual(resolve(url).func, views_trip.trip_delete)