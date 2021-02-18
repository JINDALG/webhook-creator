from django.conf.urls import re_path

from rest_framework.routers import DefaultRouter

from hooks.views import WebHookViewSet, WebHookInputView


router = DefaultRouter()
router.register('hooks', WebHookViewSet, 'hooks')

urlpatterns = router.urls + [
    re_path(r'input/(?P<key>[\w]+)/$', WebHookInputView.as_view(), name='web_hook_input')
]
