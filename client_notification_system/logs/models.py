from django.db import models
from notifications.models import Notification


class SMSLog(models.Model):
    notification = models.OneToOneField(Notification, on_delete=models.CASCADE)
    sent_at = models.DateTimeField()
    status = models.CharField(max_length=20)
    response_message = models.TextField(blank=True)
