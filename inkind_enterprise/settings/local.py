from .base import *
import sys

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# DATABASES
# ------------------------------------------------------------------------------
# This uses settings from a .env file in the project root.
# Use a simpler database for commands that don't need the full PostGIS stack.
if any(cmd in sys.argv for cmd in ["makemessages", "collectstatic"]):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    # Make sure PostgreSQL is installed and running locally.
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("POSTGRES_DB"),
            "USER": config("POSTGRES_USER"),
            "PASSWORD": config("POSTGRES_PASSWORD"),
            "HOST": config("POSTGRES_HOST", default="localhost"),
            "PORT": config("POSTGRES_PORT", default=5432, cast=int),
        }
    }

# TOOLS
# ------------------------------------------------------------------------------
# Add django-debug-toolbar for local development
# Application definition
# INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + ["debug_toolbar"]
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
# MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1"]
