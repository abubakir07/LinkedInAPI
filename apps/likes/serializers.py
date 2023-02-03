from rest_framework import serializers

from apps.likes.models import CommentLike, PostLike


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = (
            'id',
            'comment',
        )
        read_only_fields = ('owner',)


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = (
            'id',
            'post',
        )
        read_only_fields = ('owner',)
