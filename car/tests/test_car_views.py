from django.db.models import QuerySet
from django.test import TestCase, Client

from django.urls import reverse
from car.models import Car


class TestCarViews(TestCase):
    @staticmethod
    def n_cars(name=''):
        cars = Car.objects.all()

        if len(name) > 0:
            cars = cars.filter(name=name)

        return cars.count()

    def setUp(self) -> None:
        self.client = Client()

        self.name = 'test'
        Car(name=self.name, price=0, speed=0).save()
        self.pk = Car.objects.get(name=self.name).id
        self.number_of_cars = self.n_cars()

    def test_car_list_GET(self):
        url = reverse('car:car_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car/cars.html')
        self.assertIn('cars', response.context)
        self.assertIsInstance(response.context['cars'], QuerySet)
        self.assertEqual(len(response.context['cars']), 1)

    def test_car_add_POST(self):
        url = reverse('car:car_add')
        name = 'test_add'
        n_cars = self.n_cars(name)
        response = self.client.post(url, {'name': name})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.number_of_cars + 1, self.n_cars())
        self.assertEqual(n_cars + 1, self.n_cars(name))
        self.assertEqual(name, Car.objects.get(name=name).name)

    def test_car_delete_GET(self):
        url = reverse('car:car_delete', args=[self.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.number_of_cars - 1, self.n_cars())

    def test_car_put_PUT(self):
        url = reverse('car:car_put')
        response = self.client.put(url, {"pk": self.pk, "name": "test1", "price": 1000}, content_type="application/json")

        test_car = Car.objects.get(pk=self.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.number_of_cars, self.n_cars())
        self.assertEqual(test_car.name, 'test1')
        self.assertEqual(test_car.price, 1000)



