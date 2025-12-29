from django.urls import path
from .views import SMSTemplateListCreate, SMSTemplateDetail, NotificationListCreate, NotificationDetail

urlpatterns = [
    path('templates/', SMSTemplateListCreate.as_view(), name='template-list'),
    path('templates/<int:pk>/', SMSTemplateDetail.as_view(), name='template-detail'),
    path('', NotificationListCreate.as_view(), name='notification-list'),
    path('<int:pk>/', NotificationDetail.as_view(), name='notification-detail'),
]
