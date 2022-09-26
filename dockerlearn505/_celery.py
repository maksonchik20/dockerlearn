import os
from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dockerlearn505.settings')

# app = Celery('dockerlearn505')
# app.config_from_object('celeryconfig', namespace='CELERY')
# app.autodiscover_tasks()

app = Celery(broker='redis://:tY2rVVPJhokJthq5Es5aqZ3Kc5IfNxjQ@redis-13429.c267.us-east-1-4.ec2.cloud.redislabs.com:13429/0')
# app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()
@app.task(name='dockerlearn505._celery.task')
def add(x, y):
    print(x + y)
    return x + y



