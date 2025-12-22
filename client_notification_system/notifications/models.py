from django.db import models
from django.contrib.auth.models import User
from clients.models import Client


class SMSTemplate(models.Model):
    """Reusable SMS template for a user"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sms_templates'
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Notification(models.Model):
    """Scheduled SMS notification to a client"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
    ]
    
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    template = models.ForeignKey(
        SMSTemplate,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-scheduled_time']

    def __str__(self):
        return f"{self.client.name} - {self.template.title}"

