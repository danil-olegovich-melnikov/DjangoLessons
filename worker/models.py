from django.db import models
from django.contrib.auth.models import User
from worker import tasks
import random


# Create your models here.
class EmailCode(models.Model):
    code = models.CharField("Код", max_length=124)
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} {self.code}"

    def save(self, *args, **kwargs):
        self.code = str(random.randint(1000, 9999))
        # tasks.send_verification_email(email=self.user.email, code=self.code)
        print("Sended\n" * 5)
        tasks.send_verification_email.delay(email=self.user.email, code=self.code)
        super(EmailCode, self).save(*args, **kwargs)
