from rest_framework import serializers
from .models import SMSTemplate, Notification


class SMSTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSTemplate
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'client', 'template', 'scheduled_time', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']
