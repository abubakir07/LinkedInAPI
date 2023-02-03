from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Contacts
from .serializers import ContactsSerializer

class ContactsAPIViewSet(GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    # def create(self, request, *args, **kwargs):
    #     # Check if user has already created a contact
    #     user_contacts = Contacts.objects.filter(owner=request.user)
    #     if user_contacts.exists():
    #         contact_id = user_contacts[0].id
    #         return Response({'error': f'You have already created a contact. You can update your contacts http://127.0.0.1:8000/contacts/{contact_id}/'}, status=400)
        
    #     return super().create(request, *args, **kwargs)
    