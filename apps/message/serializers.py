from rest_framework import serializers

from apps.message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        read_only_fields = ('owner', )
        fields = (
            'id',
            'chat',
            'text',
            'files',
            'create_at',
        )