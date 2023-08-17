import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_signup.settings')

app = Celery('simple_signup')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()