from django.contrib import admin

from apps.chats.models import Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'companion',)
