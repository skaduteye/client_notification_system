from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SMSTemplateViewSet

router = DefaultRouter()
router.register('templates', SMSTemplateViewSet, basename='smstemplate')

urlpatterns = [
    path('', include(router.urls)),
]
