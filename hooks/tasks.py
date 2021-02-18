from datetime import timedelta
from django.utils.timezone import now

from webhook_creator_api.celery import app
from hooks.models import WebHook


@app.task
def purge_expired_webhooks():
    """
    Tasks to purge expired web-hooks.
    Deleting all web-hooks created before 1 hour
    """
    WebHook.objects.filter(created_at__lt=now() - timedelta(hours=1)).delete()
