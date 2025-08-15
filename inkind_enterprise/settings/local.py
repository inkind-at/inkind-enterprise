from .base import *

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# DATABASES
# ------------------------------------------------------------------------------
# This uses settings from a .env file in the project root.
# Make sure PostgreSQL with PostGIS is installed and running locally.
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST", default="localhost"),
        "PORT": config("POSTGRES_PORT", default=5432),
    }
}

# TOOLS
# ------------------------------------------------------------------------------
# Add django-debug-toolbar for local development
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1"]

