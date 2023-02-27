from django.contrib.auth.models import AbstractUser
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    price = models.FloatField()


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=12)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

