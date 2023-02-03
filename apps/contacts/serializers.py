from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.contacts.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = (
            'id',
            'owner',
            'members',
            'created_at',
            'updated_at'
            )
        read_only_fields = ('owner',)
