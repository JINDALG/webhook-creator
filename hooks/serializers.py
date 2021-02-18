from rest_framework import serializers

from hooks.models import WebHook, WebHookData


class WebHookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebHook
        fields = ('key', 'remaining_minutes', 'id')


class WebHookDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebHookData
        fields = ('query_params', 'headers', 'body', 'minutes', 'web_hook')
        extra_kwargs = {
            'minutes': {'read_only': True},
            'web_hook': {'write_only': True}
        }


class WebHookDetailSerializer(WebHookListSerializer):

    hits = WebHookDataSerializer(source='webhookdata_set', many=True)

    class Meta:
        model = WebHook
        fields = WebHookListSerializer.Meta.fields + ('hits',)
