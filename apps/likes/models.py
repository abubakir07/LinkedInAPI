from django.db import models
from django.contrib.auth import get_user_model

from apps.comments.models import Comment
from apps.posts.models import Post


User = get_user_model()


class Like(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_like',
        verbose_name='user_like',
    )


class PostLike(Like):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_like',
        verbose_name='post_like',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'post like'
        verbose_name_plural = 'Post likes'

    def __str__(self):
        return f'post {self.post.title}---{self.owner}'


class CommentLike(Like):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='comment_like',
        verbose_name='comment_like',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'comment like'
        verbose_name_plural = 'Comment likes'

    def __str__(self):
        return f'Comment post: {self.comment.post.title}---{self.owner}'

