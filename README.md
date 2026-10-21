[README.md](https://github.com/user-attachments/files/33759497/README.md)
# Job Portal — Django

A Django-based job portal project organized into application modules and templates. The repository includes Django's `manage.py` entry point, application folders, templates, and a SQLite database file.

## Overview

The project provides a foundation for a web-based job portal. Review the application code to confirm the exact user flows and features enabled in your copy before extending or deploying it.

## Technologies

- Python
- Django
- HTML templates
- SQLite (database file included in the repository)

## Getting started

### Prerequisites

- Python 3
- `pip`

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/winfrey-Git/Job-Portal-Django-.git
   cd Job-Portal-Django-
   ```

2. Create and activate a virtual environment:

   **Windows**
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install Django:

   ```bash
   pip install django
   ```

   If the project has a `requirements.txt` file in your local copy, install its dependencies with `pip install -r requirements.txt` instead.

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/` in your browser.

## Development notes

- Check the project's URL configuration and views to understand the available pages.
- Do not use the included SQLite database as a production database.
- Before deploying, configure environment variables, production settings, static files, and an appropriate production database.
- Do not commit passwords, secret keys, or other credentials.

## Author

**Winfred Kive**  
GitHub: [winfrey-Git](https://github.com/winfrey-Git)
