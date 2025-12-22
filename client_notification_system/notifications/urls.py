from django.urls import path
from .views import SMSTemplateListCreate, SMSTemplateDetail

urlpatterns = [
    path('templates/', SMSTemplateListCreate.as_view(), name='template-list'),
    path('templates/<int:pk>/', SMSTemplateDetail.as_view(), name='template-detail'),
]
