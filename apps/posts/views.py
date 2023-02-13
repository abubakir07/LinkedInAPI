from django.db.models import Q
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



from apps.contacts.models import Contact
from rest_framework.response import Response

class UserContactPostView(viewsets.GenericViewSet,
                           mixins.ListModelMixin,
                           mixins.RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        contacts = Contact.objects.filter(owner=self.request.user)
        contacts_ids = contacts.values_list('members', flat=True)
        return Post.objects.filter(Q(owner__in=contacts_ids))

