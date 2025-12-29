import requests
from datetime import datetime

BASE = 'http://127.0.0.1:8000'

# Login
print('=== LOGIN ===')
r = requests.post(f'{BASE}/auth/login/', json={'username': 'alxuser', 'password': 'alxpass123'})
print(f'Status: {r.status_code}')
tokens = r.json()
access_token = tokens.get('access')
headers = {'Authorization': f'Bearer {access_token}'}

# List Clients
print('\n=== LIST CLIENTS ===')
r = requests.get(f'{BASE}/clients/', headers=headers)
print(f'Status: {r.status_code}')
clients = r.json()
print(f'Response: {clients}')
client_id = clients['results'][0]['id'] if clients.get('results') else 1

# List Templates
print('\n=== LIST TEMPLATES ===')
r = requests.get(f'{BASE}/sms/templates/', headers=headers)
print(f'Status: {r.status_code}')
templates = r.json()
print(f'Response: {templates}')
template_id = templates['results'][0]['id'] if templates.get('results') else 1

# Create Notification (triggers SMS)
print('\n=== CREATE NOTIFICATION ===')
r = requests.post(f'{BASE}/sms/', json={'client': client_id, 'template': template_id, 'scheduled_time': datetime.now().isoformat()}, headers=headers)
print(f'Status: {r.status_code}')
print(f'Response: {r.json()}')

# Check Logs
print('\n=== SMS LOGS ===')
r = requests.get(f'{BASE}/logs/', headers=headers)
print(f'Status: {r.status_code}')
print(f'Response: {r.json()}')

print('\n=== ALL TESTS COMPLETE ===')
