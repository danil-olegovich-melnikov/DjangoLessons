from celery import shared_task
import time

@shared_task(name="sum_two_numbers")
def send_verification_email(email: str, code: str):
    time.sleep(10)
    print(email, code)
    return True
