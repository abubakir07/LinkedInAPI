from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Contacts(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='contact owner',
        related_name='contacts'
    )
    members = models.ManyToManyField(
        User,
        related_name='member_of',
        verbose_name='members'
        )
    created_at = models.DateTimeField(
        verbose_name='created_at',
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        verbose_name='updated_at',
        auto_now=True
        )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"ID: {self.owner.username}"
    