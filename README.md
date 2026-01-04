# Client SMS Notification System

This is my ALX Backend Capstone Project. It's a Django REST API that lets businesses manage their clients and send them SMS notifications.

## What it does

- Users can register and login to get access
- Add and manage client contacts
- Create SMS message templates
- Schedule notifications to be sent to clients
- The system sends SMS using BMS SMS API
- Background tasks handled with Celery and Redis

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

## Built with
- Django + Django REST Framework
- JWT authentication
- codeslawBMS SMS API