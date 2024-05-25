from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from authorization.managers import UserManager


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    ADMIN, CUSTOMER = 1, 2

    ROLES = (
        (ADMIN, 'admin'),
        (CUSTOMER, 'customer'),
    )

    username = models.CharField(max_length=100, unique=True)
    role = models.IntegerField(choices=ROLES, default=CUSTOMER)
    email = models.EmailField(unique=True, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = []
