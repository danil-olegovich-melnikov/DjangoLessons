from celery import shared_task
import time


@shared_task(name="send_verification_email")
def send_verification_email(email: str, code: str):
    print("Receiving")
    time.sleep(5)
    print("ENDED")
    return False
