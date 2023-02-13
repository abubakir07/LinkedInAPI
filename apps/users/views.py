from urllib import response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django.contrib.auth import get_user_model

from apps.users.models import Skills, WorkExperience, Education
from apps.users.serializers import (SkillsSerializer, UserSerializer,
                                    UserCreateSerializer, UserUpdateSerializer,
                                    UserShowSerializer, WorkExperienceSerializer,
                                    EducationSerializer,)
from utils.permissions import IsUserOwner, IsOwner


User = get_user_model()

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
    

class UserShowApiViewSet(GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserShowSerializer
    permission_classes = [AllowAny]


class SkillsApiViewSet(GenericViewSet,
                       mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]


class WorkExperienceApiViewSet(GenericViewSet,
                               mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'retrieve']:
            return [IsOwner()]
        return [IsAuthenticated()]


class EducationApiViewSet(GenericViewSet,
                          mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          mixins.DestroyModelMixin):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'retrieve']:
            return [IsOwner()]
        return [IsAuthenticated()]



