from rest_framework import mixins, viewsets, permissions
from rest_framework.response import Response

from apps.posts.models import Post
from apps.favorites.models import Favorite
from apps.favorites.serializers import FavoriteSerializers
from utils.permissions import IsOwner


class FavoriteApiViewSet(viewsets.GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Favorite.objects.filter(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["list", "retrieve", "destroy"]:
            return [IsOwner()]
        return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        post = Post.objects.get(id=request.data['post'])
        favorites = Favorite.objects.filter(post=post)
        for favorite in favorites:
            if favorite.owner == request.user:
                return Response({'Error': 'Have you already saved this post'})
        return super().create(request, *args, **kwargs)

