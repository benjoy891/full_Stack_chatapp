# Chat Application for Interest-Based Communication

## Overview

This **Chat Application** enables users to connect and communicate with others who share similar interests or niches. By allowing users to select specific categories of interest, the platform fosters meaningful interactions and niche-based discussions, creating a vibrant and engaging community.

Overview
This Chat Application enables users to connect and communicate with others who share similar interests or niches. By allowing users to select specific categories of interest, the platform fosters meaningful interactions and niche-based discussions, creating a vibrant and engaging community.

## Key Features

Key Features

- **Category-Based User Matching**: Users can choose an area of interest and join conversations with like-minded individuals.
- **Real-Time Communication**: Supports seamless, real-time messaging using WebSocket technology powered by Django Channels.
- **User Authentication**: Secure registration and login functionality to ensure a safe environment.
- **Dynamic UI**: Built with React and TypeScript, the application delivers a modern, responsive, and user-friendly interface.
- **Scalable API**: Backend developed using Django and Django REST Framework (DRF), providing robust and scalable APIs for the chat functionality.
- **Persistent Chat History**: Messages and discussions are stored securely, enabling users to access past conversations.
- **Real-Time Notifications**: Notify users about incoming messages and updates in their selected categories.

Category-Based User Matching: Users can choose an area of interest and join conversations with like-minded individuals.
Real-Time Communication: Supports seamless, real-time messaging using WebSocket technology powered by Django Channels.
User Authentication: Secure registration and login functionality to ensure a safe environment.
Dynamic UI: Built with React and TypeScript, the application delivers a modern, responsive, and user-friendly interface.
Scalable API: Backend developed using Django and Django REST Framework (DRF), providing robust and scalable APIs for the chat functionality.
Persistent Chat History: Messages and discussions are stored securely, enabling users to access past conversations.
Realtime Notifications: Notify users about incoming messages and updates in their selected categories.

## Technology Stack

### Backend:

- Django for robust server-side development.
- Django REST Framework (DRF) for API creation.
- Django Channels for real-time WebSocket communication.

Technology Stack
Backend:

### Frontend:

- React for building a dynamic and interactive user interface.
- TypeScript for type-safe, maintainable frontend code.

Django for robust server-side development.
Django REST Framework (DRF) for API creation.
Django Channels for real-time WebSocket communication.
Frontend:

### WebSocket Communication:

- Integrated real-time messaging with Django Channels.

React for building a dynamic and interactive user interface.
TypeScript for type-safe, maintainable frontend code.
WebSocket Communication:

### Database:

- Relational database for storing user data, chat messages, and categories.

Integrated real-time messaging with Django Channels.
Database:

Relational database for storing user data, chat messages, and categories.
Installation Guide
Backend Setup:

Clone the repository and navigate to the project folder.
Create a virtual environment:
bash
Copy code
python -m venv venv
Install the dependencies:
bash
Copy code
pip install -r requirements.txt
Run migrations:
bash
Copy code
python manage.py migrate
Start the development server:
bash
Copy code
python manage.py runserver
Frontend Setup:

Navigate to the frontend directory.
Install dependencies:
bash
Copy code
npm install
Start the React development server:
bash
Copy code
npm start
WebSocket Server:

Ensure the ASGI server is configured for Django Channels:
bash
Copy code
daphne -b 0.0.0.0 -p 8001 <project_name>.asgi:application
Contribution
Contributions are welcome! Please follow the guidelines outlined in the CONTRIBUTING.md file.
