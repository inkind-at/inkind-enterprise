from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """
    Custom user model to include roles.
    'Enterprise Admin' is a role, 'Superuser' is a flag.
    """
    class Roles(models.TextChoices):
        ENTERPRISE_ADMIN = 'ADMIN', _('Enterprise Admin')

    # Use email as the unique identifier
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(_('role'), max_length=50, choices=Roles.choices, default=Roles.ENTERPRISE_ADMIN)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

