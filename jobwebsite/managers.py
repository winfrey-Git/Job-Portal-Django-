from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

"""
custom manager to handle user creation where email is used as the email is used as the unique identifier.
"""


def create_user(self, email, password, **extra_fields):
    if not email:
        raise ValueError('An email address is required')
    if not password:
        raise ValueError('A password is required')
    
    email = self.normalize_email(email)
    user = self.model(email=email, password=password)
    user.set_password(password)
    user.save()
    return user

def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    if extra_fields.get('is_staff' is not True):
        raise ValueError('superuser must have is staff=True.')
    if extra_fields.get('is_superuser') is not True:
        raise ValueError('Superuser must have is_superuser=True.')
    
    return self.create_user(email, password, **extra_fields)
