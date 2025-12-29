"""
SMS service for sending messages via BMS SMS API.
"""

import os
import requests


def send_sms(phone_number: str, message: str) -> dict:
    """
    Send an SMS message using the BMS SMS API.
    
    Args:
        phone_number: Recipient phone number (e.g., '233XXXXXXXXX')
        message: SMS content to send
        
    Returns:
        dict with 'success' (bool) and 'message' (str)
    """
    api_key = os.getenv('BMS_API_KEY')
    sender_id = os.getenv('BMS_SENDER_ID')
    api_url = os.getenv('BMS_API_URL', 'https://bms.codeslaw.dev/api/v1/sms/send')
    
    if not api_key or not sender_id:
        return {
            'success': False,
            'message': 'BMS_API_KEY or BMS_SENDER_ID not configured'
        }
    
    payload = {
        'key': api_key,
        'to': phone_number,
        'from': sender_id,
        'message': message,
    }
    
    try:
        response = requests.post(api_url, data=payload, timeout=30)
        response_data = response.json()
        
        if response.status_code == 200 and response_data.get('status') == 'success':
            return {
                'success': True,
                'message': 'SMS sent successfully',
                'response': response_data
            }
        else:
            return {
                'success': False,
                'message': response_data.get('message', 'Failed to send SMS'),
                'response': response_data
            }
    except requests.RequestException as e:
        return {
            'success': False,
            'message': str(e)
        }
