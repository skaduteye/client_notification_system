from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from .models import SMSTemplate, Notification
from .serializers import SMSTemplateSerializer, NotificationSerializer
from .tasks import send_sms_notification


class SMSTemplateListCreate(generics.ListCreateAPIView):
    serializer_class = SMSTemplateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SMSTemplate.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # Check if template with this title already exists
        title = request.data.get('title')
        if title and SMSTemplate.objects.filter(title=title).exists():
            return Response(
                {'title': 'Template with this title already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SMSTemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SMSTemplateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SMSTemplate.objects.filter(user=self.request.user)


class NotificationListCreate(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(client__user=self.request.user)

    def perform_create(self, serializer):
        notification = serializer.save()
        
        # Send SMS immediately
        send_sms_notification(notification.id)


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(client__user=self.request.user)

