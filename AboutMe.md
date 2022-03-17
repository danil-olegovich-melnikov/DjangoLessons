python manage.py seed car --number=15
celery -A config  worker -l info -P gevent
docker run --name my-redis -p 6379:6379 -d redis
