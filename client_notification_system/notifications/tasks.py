"""
Tasks for sending SMS notifications.
"""

from django.utils import timezone

from .models import Notification
from .sms_service import send_sms
from logs.models import SMSLog


def send_sms_notification(notification_id: int) -> dict:
    """
    Send an SMS notification asynchronously.
    
    Args:
        notification_id: ID of the Notification to process
        
    Returns:
        dict with task result status
    """
    # Fetch the notification
    try:
        notification = Notification.objects.select_related('client', 'template').get(id=notification_id)
    except Notification.DoesNotExist:
        return {'success': False, 'message': f'Notification {notification_id} not found'}
    
    # Skip if already sent
    if notification.status == 'sent':
        return {'success': False, 'message': 'Notification already sent'}
    
    # Get client phone number and template content
    phone_number = notification.client.phone
    message_content = notification.template.content
    
    # Send the SMS
    result = send_sms(phone_number, message_content)
    
    # Update notification status
    if result['success']:
        notification.status = 'sent'
    else:
        notification.status = 'failed'
    notification.save()
    
    # Create SMS log entry
    SMSLog.objects.update_or_create(
        notification=notification,
        defaults={
            'sent_at': timezone.now(),
            'status': notification.status,
            'response_message': result.get('message', ''),
        }
    )
    
    return {
        'success': result['success'],
        'notification_id': notification_id,
        'status': notification.status,
        'message': result.get('message', '')
    }
