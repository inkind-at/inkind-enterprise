from .base import *
from .base import config

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = False
# This should be your domain name(s), e.g., ["inkind.at", "api.inkind.at"]
ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")])

# Application definition
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# DATABASES
# ------------------------------------------------------------------------------
# This will read from environment variables provided by AWS SSM Parameter Store
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": config("RDS_DB_NAME"),
        "USER": config("RDS_USERNAME"),
        "PASSWORD": config("RDS_PASSWORD"),
        "HOST": config("RDS_HOSTNAME"),
        "PORT": config("RDS_PORT"),
    }
}
DATABASES["default"]["CONN_MAX_AGE"] = config("CONN_MAX_AGE", default=60, cast=int)

# AWS S3 STORAGE
# ------------------------------------------------------------------------------
# As per DevOps requirements, static and media files are stored on S3
# AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_DEFAULT_ACL = "private"
AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME", default="eu-central-1")
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_FILE_OVERWRITE = False

from storages.backends.s3boto3 import S3Boto3Storage

# Configure static and media storage
# Static files storage (served from S3)
# Media files storage (user uploads to S3)
class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = None

class MediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = None

STORAGES = {
    "default": {
        "BACKEND": "inkind_enterprise.settings.production.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "inkind_enterprise.settings.production.StaticStorage",
    },
}

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

# SECURITY
# ------------------------------------------------------------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=True, cast=bool)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://enterprise.inkind.at', 'http://enterprise.inkind.at']


