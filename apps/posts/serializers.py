from rest_framework import serializers

from apps.comments.models import Comment
from apps.likes.models import PostLike
from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    len_comments = serializers.SerializerMethodField(read_only=True)
    len_likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        read_only_fields = ('owner',)
        fields = (
            'id',
            'owner',
            'title',
            'image',
            'description',
            'created_at',
            'updated_at',
            'len_comments',
            'len_likes',
        )

    @staticmethod
    def get_len_comments(obj):
        comments = Comment.objects.filter(post=obj.id)
        return len(comments)

    @staticmethod
    def get_len_likes(obj):
        likes = PostLike.objects.filter(post=obj.id)
        return len(likes)
