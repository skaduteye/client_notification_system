from rest_framework import serializers
from .models import SMSTemplate, Notification


class SMSTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSTemplate
        fields = ['id', 'title', 'content', 'created_at']
        read_only_fields = ['created_at']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'client', 'template', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']
