from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .models import SMSTemplate, Notification
from .serializers import SMSTemplateSerializer, NotificationSerializer
from .tasks import send_sms_notification


class SMSTemplateListCreate(generics.ListCreateAPIView):
    serializer_class = SMSTemplateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SMSTemplate.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
        
        # If scheduled_time is now or in the past, trigger SMS immediately
        if notification.scheduled_time <= timezone.now():
            try:
                send_sms_notification.delay(notification.id)
            except Exception:
                # If Celery/Redis not available, run synchronously
                send_sms_notification(notification.id)


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(client__user=self.request.user)

