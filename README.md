# Blog API with Flask

This is a simple blog application API built with Flask, SQLAlchemy, and PostgreSQL. The application supports user authentication, CRUD operations for blog posts, and pagination. And for testing the API i have used the postman.

## Features

- User authentication (registration, login, logout)
- Create, read, update, and delete blog posts
- Display a list of all blog posts with pagination
- Display a single blog post

## Requirements

- Python 3.7+
- PostgreSQL

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/raghu295/blog_api.git
   cd blog_api

2. **Create and activate a virtual environment:**
   
- python -m venv venv
- venv\Scripts\activate  # On Windows
- source venv/bin/activate  # On macOS/Linux

3. **Install the dependencies:**

- pip install -r requirements.txt

4. **Setup the Database:**

- flask db init
- flask db migrate -m "Initial migration"
- flask db upgrade

5. **Run the Application:**

- python run.py


## API Endpoints

1.**User Authentication**
**Register:**

- URL: /register
- Method: POST
- Body:
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "password123"
}

**Login:**
- URL: /login
- Method: POST
- Body:
{
    "email": "testuser@example.com",
    "password": "password123"
}

**Logout:**
- URL: /logout
- Method: POST

2.**Blog Posts**
**Get all posts with pagination:**
- URL: /posts?page=1
- Method: GET

**Get a single post:**
- URL: /post/post_id
- Method: GET

**Create a new post:**
- URL: /post
- Method: POST
- Body:
{
    "title": "My First Post",
    "content": "This is the content of my first post."
}

**Update a post:**
- URL: /post/post_id
- Method: PUT
- Body:
{
    "title": "Updated Post Title",
    "content": "This is the updated content of the post."
}

**Delete a post:**
- URL: /post/post_id
- Method: DELETE
