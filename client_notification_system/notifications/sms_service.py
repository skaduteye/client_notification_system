"""
SMS service for sending messages via BMS (CodeslawBMS) API.
https://bms.codeslaw.dev/docs
"""

import os
import requests


def send_sms(phone_number: str, message: str) -> dict:
    """
    Send an SMS message using the BMS API.
    
    Args:
        phone_number: Recipient phone number (e.g., '0201234567' or '233201234567')
        message: SMS content to send (max 918 characters)
        
    Returns:
        dict with 'success' (bool) and 'message' (str)
    """
    api_key = os.getenv('BMS_API_KEY')
    sender_id = os.getenv('BMS_SENDER_ID')
    base_url = os.getenv('BMS_API_URL', 'https://bms.codeslaw.dev/api/v1')
    
    if not api_key:
        return {
            'success': False,
            'message': 'BMS_API_KEY not configured'
        }
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    
    payload = {
        'recipients': [phone_number],
        'message': message,
    }
    
    if sender_id:
        payload['senderId'] = sender_id
    
    try:
        response = requests.post(
            f'{base_url}/sms/send',
            headers=headers,
            json=payload,
            timeout=30
        )
        response_data = response.json()
        
        if response.status_code == 200 and response_data.get('success'):
            return {
                'success': True,
                'message': 'SMS sent successfully',
                'message_id': response_data.get('data', {}).get('messageId'),
                'credits_used': response_data.get('data', {}).get('creditsUsed'),
            }
        else:
            return {
                'success': False,
                'message': response_data.get('error', 'Failed to send SMS'),
            }
    except requests.RequestException as e:
        return {
            'success': False,
            'message': str(e)
        }


def check_balance() -> dict:
    """
    Check SMS credit balance.
    
    Returns:
        dict with balance info
    """
    api_key = os.getenv('BMS_API_KEY')
    base_url = os.getenv('BMS_API_URL', 'https://bms.codeslaw.dev/api/v1')
    
    if not api_key:
        return {'success': False, 'message': 'BMS_API_KEY not configured'}
    
    try:
        response = requests.get(
            f'{base_url}/balance',
            headers={'Authorization': f'Bearer {api_key}'},
            timeout=30
        )
        response_data = response.json()
        
        if response.status_code == 200 and response_data.get('success'):
            return {
                'success': True,
                'balance': response_data.get('data', {}).get('balance'),
            }
        else:
            return {
                'success': False,
                'message': response_data.get('error', 'Failed to check balance'),
            }
    except requests.RequestException as e:
        return {'success': False, 'message': str(e)}
