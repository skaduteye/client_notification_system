from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import SMSTemplate
from .serializers import SMSTemplateSerializer


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

