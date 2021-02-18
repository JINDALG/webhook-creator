from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webhook_creator_api.settings')
app = Celery('webhook_creator')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'purge-expired-webhooks': {
        'task': 'hooks.tasks.purge_expired_webhooks',
        # Run cron every hour to purge expired webhooks
        'schedule': crontab(minute='1', hour='*', day_of_week='*'),
    },
}
