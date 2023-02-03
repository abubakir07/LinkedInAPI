from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Chat(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="sender"
    )
    companion = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="companion"
    )

    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'Chats'

    def __str__(self):
        return f'owner: {self.owner}---companion: {self.companion}'
