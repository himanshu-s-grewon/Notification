from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

# Where the downloaded files will be stored
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demonotification.settings')
# Create the app and set the broker location (RabbitMQ)
app = Celery('demonotification')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
