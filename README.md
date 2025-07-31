# Django User Registration Project

## Overview

This is a Django web application featuring user registration with email verification and Google OAuth2 login.

- User registration with mandatory email confirmation
- Login via email/password and Google account (OAuth2)
- User accounts remain inactive until email is confirmed
- User-friendly success and error messages
- Admin panel to manage users and view activation status

## Technologies Used

- Python 3.12
- Django 5.2
- django-allauth (for authentication and email verification)
- PostgreSQL (or SQLite for development)
- Bootstrap (or any CSS framework for styling)
- Docker (optional, for deployment)

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/Ismoil1212/Authorisation.git
cd Registration_project
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file and add environment variables (see .env.template for example):
```ini
SECRET_KEY=your_secret_key
DEBUG=False
DATABASE_URL=postgres://user:password@localhost:5432/dbname
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

5. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the development server:
```bash
python manage.py runserver
```
