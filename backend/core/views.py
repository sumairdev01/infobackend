from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ContactMessage
from .serializers import ContactSerializer



class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # simple: save and return friendly response
        return super().create(request, *args, **kwargs)
