from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django.contrib.auth import get_user_model

from apps.users.models import Skills
from apps.users.serializers import SkillsSerializer, UserSerializer, UserCreateSerializer, UserUpdateSerializer
from utils.permissions import IsUserOwner


User = get_user_model()

    
class SkillsAPIViewSet(GenericViewSet,
                       mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_permissions(self):

        return super().get_permissions()


class UserApiViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['list']:
            return UserSerializer
        elif self.action in ['update']:
            return UserUpdateSerializer
        return UserCreateSerializer



    def get_permissions(self):
        if self.action in ['create']:
            return [AllowAny()]
        return [IsUserOwner()]
        