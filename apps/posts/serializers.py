from rest_framework import serializers

from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer
from apps.likes.models import PostLike
from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    post_comments = CommentSerializer(many=True, read_only=True)
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
            'post_comments',
            'len_comments',
            'len_likes',
        )


    def get_len_comments(self, obj):
        comments = Comment.objects.filter(post=obj.id)
        return len(comments)

    
    def get_len_likes(self, obj):
        likes = PostLike.objects.filter(post=obj.id)
        return len(likes)
