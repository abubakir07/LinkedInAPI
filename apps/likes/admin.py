from django.contrib import admin

from apps.likes.models import CommentLike, PostLike


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('owner', 'comment',)
    list_filter = ('comment',)


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('owner', 'post',)
    list_filter = ('post',)
