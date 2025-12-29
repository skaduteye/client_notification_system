import requests
from datetime import datetime

BASE = 'http://127.0.0.1:8000'

print('='*50)
print('CLIENT NOTIFICATION SYSTEM - API TESTS')
print('='*50)

# 1. Register new user
print('\n1. REGISTER')
r = requests.post(f'{BASE}/auth/register/', json={'username': 'finaltest', 'password': 'testpass123', 'email': 'final@test.com'})
print(f'   Status: {r.status_code} {"✓" if r.status_code in [200, 201] else "✗"}')

# 2. Login
print('\n2. LOGIN')
r = requests.post(f'{BASE}/auth/login/', json={'username': 'finaltest', 'password': 'testpass123'})
print(f'   Status: {r.status_code} {"✓" if r.status_code == 200 else "✗"}')
tokens = r.json()
access_token = tokens.get('access')
headers = {'Authorization': f'Bearer {access_token}'}

# 3. Create Client
print('\n3. CREATE CLIENT')
r = requests.post(f'{BASE}/clients/', json={'name': 'Final Test Client', 'phone': '233557382057'}, headers=headers)
print(f'   Status: {r.status_code} {"✓" if r.status_code == 201 else "✗"}')
client_id = r.json().get('id')

# 4. List Clients
print('\n4. LIST CLIENTS')
r = requests.get(f'{BASE}/clients/', headers=headers)
print(f'   Status: {r.status_code} {"✓" if r.status_code == 200 else "✗"}')
print(f'   Count: {len(r.json())}')

# 5. Create Template
print('\n5. CREATE TEMPLATE')
r = requests.post(f'{BASE}/sms/templates/', json={'title': 'Final Test', 'content': 'Hello from ALX Capstone!'}, headers=headers)
print(f'   Status: {r.status_code} {"✓" if r.status_code == 201 else "✗"}')
template_id = r.json().get('id')

# 6. List Templates
print('\n6. LIST TEMPLATES')
r = requests.get(f'{BASE}/sms/templates/', headers=headers)
print(f'   Status: {r.status_code} {"✓" if r.status_code == 200 else "✗"}')
print(f'   Count: {len(r.json())}')

# 7. Create Notification
print('\n7. CREATE NOTIFICATION')
r = requests.post(f'{BASE}/sms/', json={'client': client_id, 'template': template_id, 'scheduled_time': datetime.now().isoformat()}, headers=headers)
print(f'   Status: {r.status_code} {"✓" if r.status_code == 201 else "✗"}')

# 8. List Notifications
print('\n8. LIST NOTIFICATIONS')
r = requests.get(f'{BASE}/sms/', headers=headers)
print(f'   Status: {r.status_code} {"✓" if r.status_code == 200 else "✗"}')
print(f'   Count: {len(r.json())}')

# 9. Check SMS Logs
print('\n9. SMS LOGS')
r = requests.get(f'{BASE}/logs/', headers=headers)
print(f'   Status: {r.status_code} {"✓" if r.status_code == 200 else "✗"}')
print(f'   Count: {len(r.json())}')

print('\n' + '='*50)
print('ALL API TESTS COMPLETED!')
print('='*50)
