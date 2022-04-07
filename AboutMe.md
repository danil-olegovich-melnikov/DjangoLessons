python manage.py seed car --number=15
celery -A config  worker -l info 
docker run --name redis -p 6379:6379 redis
