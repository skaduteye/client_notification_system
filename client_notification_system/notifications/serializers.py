from rest_framework import serializers
from .models import SMSTemplate


class SMSTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSTemplate
        fields = ['id', 'title', 'content', 'created_at']
        read_only_fields = ['created_at']
