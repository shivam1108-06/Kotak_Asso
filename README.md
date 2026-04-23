# Kotak & Associates — Corporate Website

A Django-based corporate website for **Kotak & Associates**, a chartered accountancy / financial advisory firm. The site presents the firm's services, team, testimonials, and provides contact and newsletter subscription functionality with email notifications.

---

## Features

- **Home, About, Benefits, Process, Team, Testimonials** — fully styled marketing pages.
- **Services catalog** — 8 detailed service pages rendered from a single template:
  - Financial Planning & Budgeting
  - Liquidity Management
  - KRA-KPI Tracking
  - Internal Control System
  - Finance Dashboards
  - AR & AP Management
  - Business Health Checkup
  - IPO Advisory
- **Contact form** — stores inquiries in the database and sends an email notification to the firm via Gmail SMTP.
- **Newsletter subscription** — collects and stores unique email subscribers.
- **Privacy Policy / Terms of Service / Custom 404** pages.
- **Django admin** for managing contact messages and newsletter subscribers.

---

## Tech Stack

- **Python** 3.10+
- **Django** 4.2.20
- **SQLite** (default development database)
- **HTML / CSS / JavaScript** (server-rendered Django templates)
- **Gmail SMTP** for transactional email

---

## Requirements

Install Python dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```
Django==4.2.20
```

---

## Project Structure

```
Kotak_Asso/
├── manage.py
├── db.sqlite3              (local dev DB — not committed)
├── requirements.txt
├── README.md
├── kotak_project/          (Django project config)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/                   (main application)
│   ├── models.py           (ContactMessage, NewsletterSubscriber)
│   ├── views.py            (all page views + form handlers + SERVICES_DATA)
│   ├── admin.py
│   └── migrations/
├── templates/              (HTML templates)
└── static/                 (CSS / JS / images)
```

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/kotak-project.git
cd kotak-project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure email (IMPORTANT)

Open `kotak_project/settings.py` and update the email settings with your own Gmail SMTP credentials:

```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-gmail-app-password'
DEFAULT_FROM_EMAIL = 'Kotak & Associates <your-email@gmail.com>'
CONTACT_NOTIFICATION_EMAIL = 'your-email@gmail.com'
```

> Use a Gmail **App Password** (not your real password). Generate one from your Google Account → Security → 2-Step Verification → App passwords.

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (to access /admin)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open your browser at: **http://127.0.0.1:8000/**

Admin panel: **http://127.0.0.1:8000/admin/**

---

## URL Routes

| URL                              | View                   | Description                         |
|----------------------------------|------------------------|-------------------------------------|
| `/`                              | `home`                 | Landing page                        |
| `/about/`                        | `about`                | About the firm                      |
| `/benefits/`                     | `benefits`             | Benefits of working with us         |
| `/services/`                     | `services`             | Services overview                   |
| `/services/<slug>/`              | `service_detail`       | Individual service detail page      |
| `/process/`                      | `process`              | Our process                         |
| `/contact/`                      | `contact`              | Contact page with form              |
| `/contact/submit/`               | `contact_submit`       | Contact form POST handler           |
| `/team/`                         | `team`                 | Team members                        |
| `/testimonials/`                 | `testimonials`         | Client testimonials                 |
| `/privacy-policy/`               | `privacy_policy`       | Privacy policy                      |
| `/terms-of-service/`             | `terms_of_service`     | Terms of service                    |
| `/newsletter/subscribe/`         | `newsletter_subscribe` | Newsletter subscription POST        |
| `/admin/`                        | Django admin           | Admin panel                         |

---

## Database Models

### `ContactMessage`
Stores contact form submissions with fields:
- `name`, `email`, `phone`, `company_name`
- `service_interested`, `budget_range`, `urgency`
- `message`, `created_at`

### `NewsletterSubscriber`
Stores unique newsletter emails:
- `email` (unique), `subscribed_at`

---

## Security Notes (for production)

Before deploying, update `settings.py`:

- Set `DEBUG = False`
- Move `SECRET_KEY` to an environment variable
- Move `EMAIL_HOST_PASSWORD` to an environment variable
- Configure `ALLOWED_HOSTS` with your domain
- Use a production-grade database (PostgreSQL / MySQL)
- Serve static files via WhiteNoise / nginx
- Enable HTTPS and set `SECURE_SSL_REDIRECT = True`

---

## License

This project is proprietary software owned by **Kotak & Associates**. All rights reserved.

---

## Contact

For any queries about this project, reach out via the contact form on the website.
