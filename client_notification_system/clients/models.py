from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    """Client contact that belongs to a user"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='clients'
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
