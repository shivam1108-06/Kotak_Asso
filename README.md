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
- **Django** 6.0.6
- **SQLite** locally, **PostgreSQL** in production (via `DATABASE_URL`)
- **Gunicorn + WhiteNoise** for serving in production
- **HTML / CSS / JavaScript** (server-rendered Django templates)
- **Gmail SMTP** for transactional email

---

## Requirements

Install Python dependencies:

```bash
pip install -r requirements.txt
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

### 4. Configure email (optional locally)

Email settings are read from environment variables (never hard-code them):

```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
CONTACT_NOTIFICATION_EMAIL=where-inquiries-should-go@example.com
```

> Use a Gmail **App Password** (not your real password). Generate one from your Google Account → Security → 2-Step Verification → App passwords. Without these, contact messages are still saved and visible in /admin; only the notification email is skipped.

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

## Deploying to Railway

The `Procfile` runs migrations and `collectstatic`, then starts Gunicorn on each deploy.

1. Create a Railway project from this GitHub repo.
2. Add a **PostgreSQL** database to the project and reference its `DATABASE_URL` in the web service.
3. Set these variables on the web service:

| Variable | Value |
|---|---|
| `SECRET_KEY` | A long random string (`python -c "import secrets; print(secrets.token_urlsafe(50))"`) |
| `DATABASE_URL` | `${{Postgres.DATABASE_URL}}` |
| `DEBUG` | `False` |
| `GA_MEASUREMENT_ID` | Your Google Analytics 4 ID, e.g. `G-XXXXXXXXXX` (optional) |
| `TRUSTED_PROXY_COUNT` | `1` on Railway; `2` if Cloudflare is in front (optional) |
| `ADMIN_URL` | Secret admin address, e.g. `ka-office-7391` (optional, default `admin`) |
| `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD` / `CONTACT_NOTIFICATION_EMAIL` | Gmail App Password settings above |
| `ALLOWED_HOSTS` / `CSRF_TRUSTED_ORIGINS` | Only needed for a custom domain, e.g. `kotakassociates.in,www.kotakassociates.in` and `https://kotakassociates.in,https://www.kotakassociates.in` (keep the `.railway.app` entries too) |

4. Create an admin account from Railway's shell: `python manage.py createsuperuser`.

In production (detected via Railway's `RAILWAY_ENVIRONMENT`, or `PRODUCTION=true` elsewhere) the app refuses to start without `SECRET_KEY` or a PostgreSQL `DATABASE_URL`, and enables HTTPS redirect, secure cookies and HSTS (`SECURE_HSTS_SECONDS`, default 3600; raise it once the domain is final).

## Admin login lockout

[django-axes](https://django-axes.readthedocs.io/) blocks an IP address from the admin login for **1 hour after 5 wrong passwords**
(a correct login clears earlier failures). Attempts are listed in the admin under **Axes**.

- Unlock immediately: `python manage.py axes_reset`
- The real visitor IP is read via `core/client_ip.py`. Set `TRUSTED_PROXY_COUNT` to the number of proxies in front
  of the site: `1` on Railway (default in production), `2` if Cloudflare is also in front.

## Blog (Insights)

Write articles in the admin panel under **Core → Blog posts → Add**.

- **Status:** *Draft* is visible only to logged-in admins (with a preview notice); *Published* makes it public.
  A future **Published at** date schedules the post.
- **Formatting:** blank line = new paragraph, `## ` = sub-heading, `- ` = bullet, `1. ` = numbered point,
  `**text**` = bold; web addresses become links. All text is escaped, so no HTML is needed or allowed.
- **Cover image:** picked from images already in the project (no uploads, so nothing is lost on redeploy).
- Pages: `/blog/`, `/blog/<slug>/`. The 3 newest posts also appear on the home page.
  New posts are added to `/sitemap.xml` automatically.

## Google Analytics

Set the `GA_MEASUREMENT_ID` environment variable (e.g. `G-XXXXXXXXXX`) on the live server.
When it is empty, no analytics code is added. Contact-form enquiries are sent to Analytics as
`generate_lead` events and newsletter sign-ups as `sign_up` events (no names or emails are sent).

## Social media links

Footer icons are driven by `SOCIAL_LINKS` at the bottom of `kotak_project/settings.py`.
Paste a full profile URL to show that icon (it is also shared with Google as an official profile); leave it empty to hide it.

---

## License

This project is proprietary software owned by **Kotak & Associates**. All rights reserved.

---

## Contact

For any queries about this project, reach out via the contact form on the website.
