"""
Django settings for kotak_project project.
"""

from pathlib import Path
import os

import dj_database_url
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# SECURITY
# ==========================

# Railway sets RAILWAY_ENVIRONMENT automatically; PRODUCTION=true forces the
# same behaviour on any other host.
IS_PRODUCTION = bool(os.getenv("RAILWAY_ENVIRONMENT")) or (
    os.getenv("PRODUCTION", "False").lower() == "true"
)

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    if IS_PRODUCTION:
        raise ImproperlyConfigured(
            "SECRET_KEY environment variable must be set in production."
        )
    SECRET_KEY = "django-insecure-local-development-key"

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    ".railway.app,.trycloudflare.com,localhost,127.0.0.1"
).split(",")

CSRF_TRUSTED_ORIGINS = os.getenv(
    "CSRF_TRUSTED_ORIGINS",
    "https://*.railway.app,https://*.trycloudflare.com"
).split(",")

# HTTPS hardening (only on the live server; local runserver is plain HTTP).
if IS_PRODUCTION:
    # Railway terminates HTTPS at its proxy and forwards this header.
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # Start HSTS small; raise it (e.g. 31536000) once the domain is final.
    SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", "3600"))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "same-origin"

# ==========================
# APPLICATIONS
# ==========================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "core",
]

# ==========================
# MIDDLEWARE
# ==========================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "kotak_project.urls"

# ==========================
# TEMPLATES
# ==========================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.site_info",
            ],
        },
    },
]

WSGI_APPLICATION = "kotak_project.wsgi.application"

# ==========================
# DATABASE
# ==========================

# Uses DATABASE_URL (Railway PostgreSQL) when set, otherwise local SQLite.
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}

if IS_PRODUCTION and DATABASES["default"]["ENGINE"].endswith("sqlite3"):
    raise ImproperlyConfigured(
        "DATABASE_URL is not set: production would use SQLite, whose data is "
        "wiped on every redeploy. Add a PostgreSQL database on Railway."
    )

# ==========================
# PASSWORD VALIDATION
# ==========================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ==========================
# INTERNATIONALIZATION
# ==========================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

# ==========================
# STATIC FILES
# ==========================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# Django 5.1+ ignores the old STATICFILES_STORAGE setting; STORAGES is required.
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ==========================
# DEFAULT PRIMARY KEY
# ==========================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==========================
# EMAIL
# ==========================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# Don't let a slow SMTP server hang the contact form request.
EMAIL_TIMEOUT = 10

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = f"Kotak & Associates <{EMAIL_HOST_USER}>"

CONTACT_NOTIFICATION_EMAIL = os.getenv(
    "CONTACT_NOTIFICATION_EMAIL",
    EMAIL_HOST_USER,
)
# ==========================
# SOCIAL MEDIA
# ==========================
# Paste the full profile URL to show that icon in the footer (and tell Google
# about the profile). Leave a value empty to hide its icon.

SOCIAL_LINKS = {
    "linkedin": "",
    "x_twitter": "",
    "facebook": "",
    "instagram": "",
}

# ==========================
# CLIENT PORTAL
# ==========================
# "Client Login" button in the menu and the portal section on the Services
# page link here. Set to "" to hide both.

CLIENT_PORTAL_URL = os.getenv("CLIENT_PORTAL_URL", "https://veritai.ai/login")

# ==========================
# ADMIN
# ==========================
# Address of the admin login. On the live site set ADMIN_URL to something
# hard to guess (e.g. "ka-office-7391/") so bots don't find the login page.

ADMIN_URL = os.getenv("ADMIN_URL", "admin/").strip("/") + "/"

# ==========================
# GOOGLE ANALYTICS
# ==========================
# Google Analytics 4 "Measurement ID" (looks like G-XXXXXXXXXX). Analytics is
# only added to the pages when this is set, so set it only on the live site.

GA_MEASUREMENT_ID = os.getenv("GA_MEASUREMENT_ID", "").strip()
