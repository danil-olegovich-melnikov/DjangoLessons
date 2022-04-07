from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Populate database with data'

    def handle(self, *args, **options):
        print("Starting populating")

        username = "useruser"
        if User.objects.filter(username=username).exists():
            print("DB has been already populated")
            return

        user = User.objects.create_user(
            username=username,
            email=f'{username}@mail.ru',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(username)
        user.save()
        print("DB was successfully populated")


