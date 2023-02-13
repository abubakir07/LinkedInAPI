from django.db import models
from django.contrib.auth import get_user_model

from apps.chats.models import Chat


User = get_user_model()


class Message(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='sender',
        related_name='message_sender',
        null=True,
    )
    text = models.CharField(
        max_length=500,
        blank=True
    )
    files = models.FileField(
        verbose_name='files',
        blank=True
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        verbose_name='chat_messege',
        related_name="chat_messege"
    )
    create_at = models.DateTimeField(
        verbose_name='create_at',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'Messages'
        ordering = ('-create_at',)

    def __str__(self):
        return f'sender: {self.sender}---message:{self.text}'
