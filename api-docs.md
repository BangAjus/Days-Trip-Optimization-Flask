# API Documentation
This is the API documentation of Day Trips Optimization Back End Server.

## Table of Contents
- [Endpoints](#endpoints)
    - [Index](#1-index)
    - [Optimization](#2-optimization)
- [Error Responses](#error-responses)

## Endpoints
### 1. **Index**
**URL:** `/`

**Request Method:** `GET`

**Header:**
- Authorization: Bearer `<SECRET_KEY>`

**Response:**
```json
{
    "status" : {
        "code" : 200,
        "message" : "Welcome to the Back-End server of Day Trips Optimization!"
    },
    "data" : null
}
```

### 2. Optimization
**URL:** `/`

**Request Method:** `POST`

**Header:**
- Authorization: Bearer `<SECRET_KEY>`

**Example Request Body:**
```json
{
    "days" : 3,
    "data": [
        {
            "latitude": 3.5952,
            "longitude": 98.6722,
            "location_name": "Medan"
        },
        {
            "latitude": 2.9664,
            "longitude": 99.0613,
            "location_name": "Pematang Siantar"
        },
        {
            "latitude": 2.6617,
            "longitude": 98.9392,
            "location_name": "Parapat"
        },
        {
            "latitude":  2.6719,
            "longitude": 98.8532,
            "location_name": "Tuk Tuk"
        }
    ]
}
```

**Example Response:**
```json
// TBA
```

## Error Responses
### 401 Unauthorized
```json
{
    "status": {
            "code": 401,
            "message": "Unauthorized Access!"
    },
    "data": null
}
```

### 400 Bad Request
```json
{
    "status": {
            "code": 400,
            "message": "Client side error!"
        },
    "data": null
}
```

### 404 Not Found
```json
{
    "status": {
            "code": 404,
            "message": "URL not found!"
        },
        "data": null
}
```

### 405 Request Method Not Allowed
```json
{
    "status": {
            "code": 405,
            "message": "Request method not allowed!"
        },
    "data": null
}
```

### 500 Server Error
```json
{
    "status": {
            "code": 500,
            "message": "Server error!"
        },
    "data": null
}
```