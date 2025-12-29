from django.urls import path
from .views import SMSLogList

urlpatterns = [
    path('', SMSLogList.as_view(), name='smslog-list'),
]
