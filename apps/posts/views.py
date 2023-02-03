from rest_framework import mixins, viewsets, permissions

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from utils.permissions import IsOwner


class PostApiViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'destroy']:
            return [IsOwner()]
        return [permissions.IsAuthenticated()]
