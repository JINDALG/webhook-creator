from django.utils.timezone import now
from datetime import timedelta

from django.db import models


class WebHook(models.Model):
    """
    Model to store Webhook
    """
    key = models.SlugField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.key}-{self.created_at}'

    @property
    def get_hit_count(self) -> int:
        return self.webhookdata_set.all().count()

    @property
    def remaining_minutes(self) -> int:
        return int((self.created_at + timedelta(hours=1) - now()).total_seconds()//60)


class WebHookData(models.Model):
    """
    Model to store web hooks hits
    """
    web_hook = models.ForeignKey('hooks.WebHook', on_delete=models.CASCADE)
    query_params = models.TextField(blank=True)
    body = models.TextField(blank=True)
    headers = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.web_hook}'

    @property
    def minutes(self) -> int:
        return int((now() - self.created_at).total_seconds()//60)
