from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True, null=False)
    name = models.CharField(max_length=100, null=False)
    contact_number = models.CharField(max_length=100, null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    otp_verify = models.BooleanField(default=False)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =["name", "contact_number"]