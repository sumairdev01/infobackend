from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework import routers
from core.views import ContactViewSet

router = routers.DefaultRouter()

router.register(r'contact', ContactViewSet, basename='contact')

def health_check(request):
    return JsonResponse({"status": "ok", "message": "Backend is running"})

urlpatterns = [
    path('', health_check),  # Root health check
    path('health/', health_check),  # Health check endpoint
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
