import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField("Название", max_length=100)
    price = models.PositiveSmallIntegerField("Цена")
    speed = models.PositiveSmallIntegerField("Скорость")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Car: {self.name}"

    def total_number_km(self):
        return str(sum(trip.number_of_km for trip in Trip.objects.filter(car=self)))


class Trip(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    number_of_km = models.PositiveSmallIntegerField('Число проехавших километров')
    date = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.car} - {self.date} - {self.number_of_km} км"
