# Health Tracking Application

## Overview
The Health Tracking Application is a microservices-based system designed to help users monitor their health metrics, manage notifications, and track overall wellness. The project consists of three core services: **Notification Service**, **User Management Service**, and **Tracking Service**. This project leverages modern tools and frameworks to ensure scalability, reliability, and ease of use.

---
## Architecture  
The Health Tracking App consists of the following microservices and infrastructure components:  

### 1. **Auth Service (Port 8001)**  
- **Endpoints:**  
  - `/auth/register`: User registration  
  - `/auth/login`: User login  
- **Features:**  
  - Issues JWT tokens with user `{ id, username }`.  
  - Manages user authentication and authorization.  
  - Queries and stores user data in MySQL.  

---

### 2. **MySQL (Container: db)**  
- **Purpose:**  
  - Stores two collections: `Users` and `HealthData`.  
  - Accessed internally by **Auth Service**, **Tracking Service**, and **Notification Service**.  

---

### 3. **Tracking Service (Port 8002)**  
- **Endpoints:**  
  - `/track/add`: Add health tracking data (e.g., steps, calories, etc.).  
  - `/track/history`: Retrieve user's health tracking history.  
- **Features:**  
  - Persists user health data in MySQL.  
  - Publishes "new_health_data" events to RabbitMQ for notifications.  

---

### 4. **Notification Service (Port 8003)**  
- **Endpoints:**  
  - `/notify/send`: Send custom notifications to users.  
  - `/notify/subscribe`: Subscribe to health tracking events.  
- **Features:**  
  - Subscribes to "new_health_data" events from RabbitMQ.  
  - Delivers reminders and notifications in real-time based on user activity.  
  - Resolves recipient username -> userId via Auth Service.  

---

## Communication Workflow  
1. **Auth Service** validates and stores user credentials in MySQL.  
2. **Tracking Service** reads/writes user health data and publishes events to RabbitMQ.  
3. **RabbitMQ** handles "new_health_data" events via a fanout exchange and broadcasts them.  
4. **Notification Service** subscribes to RabbitMQ and delivers notifications in real-time.  

---

## Deployment  
Each microservice runs in its own Docker container, with MongoDB and RabbitMQ configured as separate containers.  

### **Ports**  
- Auth Service: `8001`  
- Tracking Service: `8002`  
- Notification Service: `8003`  
- RabbitMQ: `5672` (AMQP), `15672` (Management UI)  


---

## Folder Structure

This repository is organized into three main services: Notification Service, User Management Service, and Tracking Service. Below is the folder structure for the project:

```plaintext
health_tracking_app/
├── notification_service/
│   ├── controllers/        
│   ├── models/             
│   ├── repositories/       
│   └── services/           
│
├── user_management_service/
│   ├── controllers/        
│   ├── models/             
│   ├── repositories/       
│   └── services/           
│
└── tracking_service/
    ├── controllers/            
    ├── models/                 
    ├── repositories/           
    └── services/
```  

---

## Features

- **Notification Management**: Send timely health-related notifications and reminders.
- **User Management**: Handle user registration, profile updates, and authentication.
- **Health Tracking**: Monitor health metrics like heart rate, sleep, and activity.

---

## Technology Stack

- **Programming Language**: Python
- **Framework**: Django
- **Database**: MySQL
- **Authentication**: JWT-based authentication

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```  
2. Navigate to the project directory:
   ```bash
   cd health_tracking_app
   ```  
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```  
4. Set up the database:
   - Configure PostgreSQL.
   - Run the database migrations for each service.
5. Start each service:
   ```bash
   python notification_service/main.py  
   python user_management_service/main.py  
   python tracking_service/main.py  
   ```  
6. Test the endpoints using Postman or any API testing tool.

---

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```  
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```  
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```  
5. Create a pull request.

---

## API Documentation



---

## Microservices Overview

| Service               | Port | Purpose                                                                  | Key Features                                                                           | Database Entities            | APIs                                                                                           |
|-----------------------|------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------|------------------------------|-----------------------------------------------------------------------------------------------|
| Notification Service  | 8001 | Manages health-related notifications and reminders.                     | - Send notifications.<br>- Schedule reminders.<br>- Manage notification preferences. | Notifications               | - POST /notifications: Create a notification.<br>- GET /notifications: Retrieve notifications. |
| User Management Service | 8002 | Handles user registration, authentication, and profile management.      | - Register and manage users.<br>- JWT-based authentication.<br>- Role-based access.  | Users, Roles, Profiles       | - POST /users: Create user.<br>- GET /users: Retrieve user.<br>- PUT /users: Update user.        |
| Tracking Service      | 8003 | Tracks and monitors health metrics like heart rate and sleep patterns.  | - Record health metrics.<br>- Generate reports.<br>- Provide insights.               | Metrics, Activities          | - POST /track: Record metrics.<br>- GET /track: Retrieve metrics.<br>- DELETE /track/id: Delete metrics. |
