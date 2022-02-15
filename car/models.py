from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField("Название", max_length=100)
    price = models.PositiveSmallIntegerField("Цена")
    speed = models.PositiveSmallIntegerField("Скорость")

    def __str__(self):
        return f"Car: {self.name}"
