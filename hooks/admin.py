from django.contrib import admin

from hooks.models import WebHook, WebHookData

admin.site.register(WebHook)
admin.site.register(WebHookData)
