from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import SMSLog
from .serializers import SMSLogSerializer


class SMSLogList(generics.ListAPIView):
    """Read-only list of SMS logs for authenticated user."""
    serializer_class = SMSLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SMSLog.objects.filter(
            notification__client__user=self.request.user
        ).select_related('notification__client', 'notification__template')
