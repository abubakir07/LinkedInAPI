from rest_framework import mixins, viewsets, permissions

from apps.likes.models import PostLike, CommentLike
from apps.likes.serializers import PostLikeSerializer, CommentLikeSerializer
from utils.permissions import IsOwner


class PostLikeViewSet(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["list", "retrieve", "destroy"]:
            return [IsOwner()]
        return [permissions.IsAuthenticated()]


class CommentLikeViewSet(viewsets.GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["retrieve", "destroy"]:
            return [IsOwner()]
        return [permissions.IsAuthenticated()]
