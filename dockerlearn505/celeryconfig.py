REDIS_HOST = 'redis-13429.c267.us-east-1-4.ec2.cloud.redislabs.com'
REDIS_PORT = 13429
REDIS_PASSWORD = 'tY2rVVPJhokJthq5Es5aqZ3Kc5IfNxjQ'

CELERY_BROKER_URL = 'redis://:tY2rVVPJhokJthq5Es5aqZ3Kc5IfNxjQ@redis-13429.c267.us-east-1-4.ec2.cloud.redislabs.com:13429/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://:tY2rVVPJhokJthq5Es5aqZ3Kc5IfNxjQ@redis-13429.c267.us-east-1-4.ec2.cloud.redislabs.com:13429/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_IMPORTS=("tasks", '_celery')