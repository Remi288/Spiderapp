from celery import Celery
from decouple import config

app = Celery('celery', broker=config('CELERY_BROKER'), include=['spider'])