from os import environ


broker_url = environ['CELERY_BROKER']
result_backend = environ['CELERY_RESULT_BACKEND']
