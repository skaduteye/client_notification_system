# Client SMS Notification System

This is my ALX Backend Capstone Project. It's a Django REST API that lets businesses manage their clients and send them SMS notifications.

## What it does

- Users can register and login to get access
- Add and manage client contacts
- Create SMS message templates
- Schedule notifications to be sent to clients
- The system sends SMS using BMS SMS API
- Background tasks handled with Celery and Redis

## Setup

First clone it:
```
git clone https://github.com/skaduteye/client_notification_system.git
cd client_notification_system
```

Install requirements:
```
pip install -r requirements.txt
```

Create a `.env` file with your SMS credentials:
```
BMS_API_KEY=your_api_key
BMS_SENDER_ID=your_sender_id
```

Run migrations and start:
```
cd client_notification_system
python manage.py migrate
python manage.py runserver
```

If you want background SMS sending, start Redis and Celery:
```
celery -A client_notification_system worker -l info
```

## API Endpoints

**Auth:**
- POST `/auth/register/` - create account
- POST `/auth/login/` - get token

**Clients:**
- GET/POST `/clients/` - list or add clients
- GET/PUT/DELETE `/clients/<id>/` - manage a client

**SMS:**
- GET/POST `/sms/templates/` - message templates
- GET/POST `/sms/` - notifications
- GET `/logs/` - see what was sent

## How to use

1. Register at `/auth/register/` with username, password, email
2. Login at `/auth/login/` to get your token
3. Use the token in headers: `Authorization: Bearer <token>`
4. Create a client, create a template, then create a notification

When you create a notification with a past or current time, it sends the SMS right away.

## Built with

- Django + Django REST Framework
- JWT authentication
- Celery + Redis for background tasks
- BMS SMS API

## Author

Samuel Aduteye - ALX Backend