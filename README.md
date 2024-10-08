# Task Manager RESTful API

## Overview
The Task Manager RESTful API is a robust and scalable application designed to help users manage their tasks efficiently. This API allows users to create, read, update, and delete tasks, making it a versatile tool for personal or team productivity.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework in Python.
- **MongoDB**: A NoSQL database for storing task data.
- **Flask-PyMongo**: A Flask extension for working with MongoDB.
- **Marshmallow**: A library for object serialization and deserialization.
- **JWT (JSON Web Token)**: For secure user authentication.
- **Python**: The programming language used to develop the API.

## Features
- User registration and authentication using JWT.
- CRUD operations for tasks (Create, Read, Update, Delete).
- Task filtering by user and status.
- Error handling for better user experience.
- API documentation with Postman for easy exploration.

## Getting Started

### Prerequisites
- Python 3.x
- MongoDB

### Installation
## 1. Clone the repository:
   ```b
   git clone https://github.com/Solexgreat/Task-Manager-Restful-API.git
   ```
## Navigate to the project directory:
```
cd Task-Manager-Restful-API
```
## Create a virtual environment (optional but very recommended):
```
python -m venv venv
```
## Activate the virtual environment:
On Windows:
```
venv\Scripts\activate
```
On macOS/Linux:
```
source venv/bin/activate
```
## Install the required packages:
```
pip install -r requirements.txt
```
## Configuration
### Set up your MongoDB connection string in the config.py file:
```python
MONGO_URI = "mongodb://<username>:<password>@localhost:27017/task_manager"
```
### Create the necessary collections in your MongoDB database.
### Running the Application
Run the application using:

```bash
python app.py
```
The API will be available at ```http://localhost:5000.```

## API Endpoints
- POST /api/auth/register: Register a new user.
- POST /api/auth/login: Authenticate user and retrieve JWT.
- GET /api/tasks: Retrieve all tasks for the authenticated user.
- POST /api/tasks: Create a new task.
- GET /api/tasks/<task_id>: Retrieve a specific task by ID.
- PUT /api/tasks/<task_id>: Update a task by ID.
- DELETE /api/tasks/<task_id>: Delete a task by ID.
  
## Contributing
Contributions are appreciated, you can submit a pull request or open an issue to discuss improvements or suggestions.

## Acknowledgments
- Flask Documentation
- MongoDB Documentation



