from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        read_only_fields = ('owner',)
        fields = (
            'id',
            'owner',
            'members',
            'created_at',
            'updated_at'
            )
