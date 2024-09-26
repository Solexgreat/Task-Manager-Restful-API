# Task Manager RESTful API

![Task Manager API](https://img.shields.io/badge/Node.js-12.0.0-green) ![MongoDB](https://img.shields.io/badge/MongoDB-v4.2.0-yellowgreen)

## Description

The **Task Manager RESTful API** is a backend application designed to manage tasks efficiently. It allows users to create, read, update, and delete tasks, enabling smooth task management. This API is built with **Node.js**, **Express.js**, and **MongoDB**, providing a robust framework for handling data and requests.

## Features

- **User Authentication**: Secure user registration and login using JWT.
- **Task Management**: Create, read, update, and delete tasks.
- **User-Specific Tasks**: Each user can manage their own tasks.
- **Data Validation**: Input validation using [Joi](https://joi.dev/) for robust error handling.
- **Environment Configuration**: Easy configuration using a `.env` file.

## Technologies Used

- **Node.js**: JavaScript runtime for server-side scripting.
- **Express.js**: Web application framework for Node.js.
- **MongoDB**: NoSQL database for storing task and user data.
- **Mongoose**: ODM library for MongoDB and Node.js.
- **Joi**: Validation library for JavaScript objects.

## Getting Started

### Prerequisites

- Node.js (12.x or higher)
- MongoDB (Local or Atlas)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Solexgreat/Task-Manager-Restful-API.git
   cd Task-Manager-Restful-API
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file in the root directory and add your MongoDB URI:
   ```
   MONGODB_URI=your_mongodb_connection_string
   JWT_SECRET=your_jwt_secret
   ```

4. Start the server:
   ```bash
   npm start
   ```

5. The API will be running on `http://localhost:3000`.

## API Endpoints

### User Authentication

- **POST** `/api/users` - Register a new user
- **POST** `/api/users/login` - Login an existing user

### Task Management

- **GET** `/api/tasks` - Get all tasks for the authenticated user
- **GET** `/api/tasks/:id` - Get a task by ID
- **POST** `/api/tasks` - Create a new task
- **PATCH** `/api/tasks/:id` - Update a task by ID
- **DELETE** `/api/tasks/:id` - Delete a task by ID

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss improvements or features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Express](https://expressjs.com/)
- [MongoDB](https://www.mongodb.com/)
- [Mongoose](https://mongoosejs.com/)
- [Joi](https://joi.dev/)
