from rest_framework import serializers

from apps.comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        read_only_fields = ('owner',)
        fields = (
            'id',
            'owner',
            'comment',
            'parent',
            'post'
        )
