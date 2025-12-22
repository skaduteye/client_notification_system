from django.db import models
from notifications.models import Notification


class SMSLog(models.Model):
    """Log entry for each SMS send attempt"""
    STATUS_CHOICES = [
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    ]
    
    notification = models.ForeignKey(
        Notification,
        on_delete=models.CASCADE,
        related_name='logs'
    )
    sent_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    response_message = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f"Log {self.id} - {self.status}"
