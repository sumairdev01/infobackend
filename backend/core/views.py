from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db import OperationalError
from .models import ContactMessage
from .serializers import ContactSerializer



class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except OperationalError:
            return Response(
                {"error": "Database not configured. Please run migrations."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except OperationalError:
            return Response(
                {"error": "Database not configured. Please run migrations."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
