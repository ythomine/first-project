from pathlib import Path

from revenue_app.config.environment import load_environment

environment = load_environment()

SECRET_KEY = environment.secret_key.get_secret_value()
DEBUG = environment.debug
ALLOWED_HOSTS = environment.allowed_hosts
CSRF_TRUSTED_ORIGINS = environment.csrf_trusted_origins

INSTALLED_APPS = ["django.contrib.staticfiles", "revenue_app.web"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "revenue_app.config.urls"
WSGI_APPLICATION = "revenue_app.config.wsgi.application"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": ["django.template.context_processors.request"]},
    }
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": environment.db_host,
        "PORT": environment.db_port,
        "NAME": environment.db_name,
        "USER": environment.db_user,
        "PASSWORD": environment.db_password.get_secret_value(),
        "CONN_MAX_AGE": 0,
    }
}
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "UTC"
USE_TZ = True
STATIC_URL = "/static/"
STATIC_ROOT = Path.cwd() / "staticfiles"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_SSL_REDIRECT = not DEBUG
SECURE_HSTS_SECONDS = 0 if DEBUG else 31536000
