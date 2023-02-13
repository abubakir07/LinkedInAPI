from rest_framework import serializers

from apps.chats.models import Chat
from apps.message.serializers import MessageSerializer

class ChatSerializer(serializers.ModelSerializer):
    chat_messege = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Chat
        fields = (
            'id',
            'owner',
            'companion',
            'chat_messege',
            )
        read_only_fields = ('owner',)

    def create(self, validated_data):
        companion = validated_data['companion']
        if Chat.objects.filter(owner=self.context['request'].user, companion=companion).exists():
            raise serializers.ValidationError("Chat already exists.")
        return Chat.objects.create(**validated_data)
