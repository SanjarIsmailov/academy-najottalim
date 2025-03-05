from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field must be set")

        extra_fields.setdefault("email", email)  # 👈 Ensure email is included
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(phone_number, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)  # 👈 Added email field
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ["email"]  # 👈 Email is now required

    def __str__(self):
        return self.phone_number
