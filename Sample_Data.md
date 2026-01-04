# Client Notification System

API Test Data & Documentation

---

## Base URL
```
http://127.0.0.1:8000
```

---

## Authentication Endpoints

### POST `/auth/register/`

Register a new user account

**Request Body:**
```json
{
  "username": "Sam",
  "email": "sam@codeslaw.dev",
  "password": "SecurePass123!"
}
```

### POST `/auth/login/` 

Login and get JWT tokens

**Request Body:**
```json
{
  "username": "Sam",
  "password": "SecurePass123!"
}
```

**Response (Save the access token!):**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

After login, use the `access` token in all subsequent requests:
> 
> Header: `Authorization: Bearer {access_token}`

---

## Client Endpoints

### GET `/clients/`

List all clients (requires authentication)

**Response:**
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "John Doe",
      "phone": "233241234567",
      "created_at": "2026-01-04T10:30:00Z"
    }
  ]
}
```

---

### POST `/clients/`

Create a new client

**Test Data 1:**
```json
{
  "name": "Sam",
  "phone": "2333557382057"
}
```

**Test Data 2:**
```json
{
  "name": "Emma",
  "phone": "233545248217"
}
```

**Test Data 3:**
```json
{
  "name": "Kwame Mensah",
  "phone": "233201234567"
}
```

**Test Data 4:**
```json
{
  "name": "Ama Asante",
  "phone": "233549876543"
}
```

---

### GET `/clients/{id}/`

Get a specific client by ID

---

### PATCH `/clients/{id}/`

Update a client

**Request Body:**
```json
{
  "name": "John Doe Jr."
}
```

---

### DELETE `/clients/{id}/`

Delete a client

---

### 🧪 Test Case: Duplicate Phone Number

Try creating another client with phone "233545248217" → Should return **400 Bad Request**

```json
{"phone": "Phone number already exists"}
```

---

## 📝 SMS Template Endpoints

### GET `/sms/templates/`

List all SMS templates

---

### POST `/sms/templates/`

Create a new SMS template

**Template 1: Welcome Message**
```json
{
  "title": "Welcome Message",
  "content": "Welcome to our service! We're glad to have you with us."
}
```

**Template 2: Payment Confirmation**
```json
{
  "title": "Payment Confirmation",
  "content": "Your payment has been received successfully. Thank you for your business!"
}
```

### GET `/sms/templates/{id}/`

Get a specific template by ID

---

### PATCH `/sms/templates/{id}/`

Update a template

**Request Body:**
```json
{
  "content": "Welcome to our premium service! We're thrilled to have you with us."
}
```

### DELETE `/sms/templates/{id}/`

Delete a template

---

## 📨 Notification (SMS Send) Endpoints

### GET `/sms/`

List all notifications

---

### POST `/sms/`

Send an SMS

**Send SMS:**
```json
{
  "client": 1,
  "template": 1
}

**Response:**
```json
{
  "id": 5,
  "client": 1,
  "template": 1,
  "status": "pending",
  "created_at": "2026-01-04T14:30:00Z"
}
```

## 📊 SMS Logs Endpoints

### GET `/logs/`

View all SMS logs (delivery status)

**Response:**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "notification": 1,
      "sent_at": "2026-01-04T14:30:05Z",
      "status": "sent",
      "response_message": "SMS sent successfully"
    }
  ]
}
```

---

## 🔄 Test Flow Sequence

1. Register a new user at `/auth/register/`
2. Login at `/auth/login/` and save the **access token**
3. Add the token to all requests: `Authorization: Bearer {token}`
4. Create 3-4 clients with different phone numbers
5. Create 3-5 SMS templates with various messages
6. List clients at `/clients/` and note the IDs
7. List templates at `/sms/templates/` and note the IDs
8. Send SMS using client ID + template ID combinations at `/sms/`
9. Check logs at `/logs/` to verify SMS delivery


## ℹ️ Additional Information

**Phone Number Format:** Use Ghana format starting with 233 (e.g., 233241234567 or 233557382057)

**SMS Sender ID:** Configured as "SMSOptics" in .env file

**BMS API:** Using https://bms.codeslaw.dev/api/v1 for SMS delivery

**JWT Token Lifetime:** Access token valid for 1 hour, refresh token for 7 days

**Pagination:** All list endpoints return 10 items per page by default