from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
# Create your models here.

class AccountUserManager(UserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """ Creates and saves a User with the given email and password. """
        now = timezone.now()
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()

        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user=self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountUserManager()

    