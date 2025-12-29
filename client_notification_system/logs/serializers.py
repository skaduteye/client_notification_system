from rest_framework import serializers
from .models import SMSLog


class SMSLogSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='notification.client.name', read_only=True)
    template_title = serializers.CharField(source='notification.template.title', read_only=True)
    
    class Meta:
        model = SMSLog
        fields = ['id', 'notification', 'client_name', 'template_title', 'sent_at', 'status', 'response_message']
