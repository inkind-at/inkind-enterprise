"""
Base settings to build other settings files upon.
"""
from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# inkind-enterprise/
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# inkind-enterprise/apps/
APPS_DIR = BASE_DIR / "apps"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# GENERAL
# ------------------------------------------------------------------------------
# The .env file should be placed in the project root (inkind-enterprise/)
# For the .envs/ structure, you would typically load these files
# into the environment using your deployment tool (e.g., docker-compose's env_file)
# and decouple will read them from the environment.
SECRET_KEY = config("DJANGO_SECRET_KEY")


# Application definition
# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",  # For PostGIS
]
THIRD_PARTY_APPS = [
    "storages",  # For S3 file storage
]
LOCAL_APPS = [
    "apps.core",
    "apps.users",
    "apps.enterprises",
    "apps.storage",
    "apps.inventory",
    "apps.needs",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLS
# ------------------------------------------------------------------------------
ROOT_URLCONF = "inkind_enterprise.urls"
WSGI_APPLICATION = "inkind_enterprise.wsgi.application"

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# INTERNATIONALIZATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATICFILES_DIRS = [str(BASE_DIR / "static")]

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = str(APPS_DIR / "media")

# DEFAULTS
# ------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "users.User"
