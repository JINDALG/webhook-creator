from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, response, status
from rest_framework.generics import CreateAPIView

from hooks import serializers as hook_serializers
from hooks.models import WebHook


class WebHookViewSet(
    viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin
):
    """
    Viewset for creating and viewing webhooks
    """
    queryset = WebHook.objects.all()

    def get_serializer_class(self):
        """
        Using separate serializer for detail view to add hits data for webhook
        :return:
        """
        if self.action == 'retrieve':
            return hook_serializers.WebHookDetailSerializer
        return hook_serializers.WebHookListSerializer


class WebHookInputView(CreateAPIView):
    """
    Viewset for testing web-hooks. This end point will be called for web-hook consumer
    """
    serializer_class = hook_serializers.WebHookDataSerializer

    def get_object(self):
        return get_object_or_404(
            WebHook, key=self.kwargs['key']
        )

    def create(self, request, *args, **kwargs):
        data = {
            'body': request.data and str(request.data) or '',
            'query_params': request.query_params and str(request.query_params) or '',
            'headers': str(request.headers),
            'web_hook': self.get_object().id
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
