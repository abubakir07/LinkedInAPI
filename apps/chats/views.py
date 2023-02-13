from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from django.db.models import Q

from apps.chats.models import Chat
from apps.chats.serializers import ChatSerializer
from apps.contacts.models import Contact


User = get_user_model()


class ChatApiViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)\
        
    def get_queryset(self):
        return Chat.objects.filter(Q(owner=self.request.user) | Q(companion=self.request.user))


    def create(self, request, *args, **kwargs):
        # get the list of companion IDs from the request data
        companion = [int(i) for i in request.data.get('companion',)]
        if Contact.objects.filter(owner=request.user, members__id__in=companion).exists():
            return super().create(request, *args, **kwargs)
        return Response({'Error': 'You do not have in contact list any user!'})
    


