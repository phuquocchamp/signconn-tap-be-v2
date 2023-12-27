from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have an username")
        account = self.model(username=username, **extra_fields)
        account.set_password(password)
        account.save(using=self._db)

        return account

    def create_superuser(self, username, password):
        account = self.create_user(username, password)
        account.is_staff = True
        account.is_superuser = True

        account.save(using=self._db)
        return account


# Create your models here.
class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
