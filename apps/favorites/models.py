from django.db import models
from django.contrib.auth import get_user_model

from apps.posts.models import Post


User = get_user_model()


class Favorite(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_favorite',
        verbose_name='Post'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='owner'
    )

    class Meta:
        verbose_name = 'favorite'
        verbose_name_plural = 'Favorite'

    def __str__(self):
        return f'Owner: {self.owner}---{self.post}'
