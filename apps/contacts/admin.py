from django.contrib import admin

from apps.contacts.models import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'created_at', 'updated_at')
