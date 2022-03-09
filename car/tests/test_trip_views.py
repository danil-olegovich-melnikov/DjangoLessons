from django.core.paginator import Page
from django.db.models import QuerySet
from django.test import TestCase, Client

from django.urls import reverse
from car.models import Car, Trip


class TestCarViews(TestCase):
    @staticmethod
    def n_trips(car=0):
        trips = Trip.objects.all()

        if car > 0:
            trips = trips.filter(car=car)

        return trips.count()

    def setUp(self) -> None:
        self.client = Client()

        self.car_name = 'test_car'
        self.number_of_km = 999

        car = Car(name=self.car_name, price=0, speed=0)
        car.save()
        self.car_pk = Car.objects.get(name=self.car_name).id

        Trip(car=car, number_of_km=self.number_of_km).save()
        self.trip_pk = Trip.objects.get(car=car).id

        self.number_of_trips = self.n_trips()

    def test_trip_list_GET(self):
        url = reverse('car:trip_list', args=[self.car_pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car/trips.html')
        self.assertIsInstance(response.context['trips'], Page)

    def test_trip_delete_GET(self):
        url = reverse('car:trip_delete', kwargs={'pk': self.car_pk, 'pk_trip': self.trip_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.n_trips(), self.number_of_trips - 1)
        self.assertEqual(self.n_trips(self.car_pk), 0)

    def test_trip_add_POST(self):
        number_of_km = 20
        car_name = "test_add_trip"
        car = Car(name=car_name, price=0, speed=0)
        car.save()
        car_pk = Car.objects.get(name=car_name).id

        url = reverse('car:trip_add', args=[car_pk])
        response = self.client.post(url, {'number_of_km': number_of_km})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.number_of_trips + 1, self.n_trips())
        self.assertEqual(1, self.n_trips(car_pk))

        trips = Trip.objects.filter(car=car)
        self.assertEqual(trips[0].number_of_km, number_of_km)