from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer
from utils.permissions import IsOwner


class CommentApiViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["list", "retrieve", "destroy"]:
            return [IsOwner()]
        return [IsAuthenticated()]

