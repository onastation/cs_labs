from django.db import models
from django_cryptography.fields import encrypt


class Login(models.Model):
    email = encrypt(models.EmailField())
    password = models.CharField(max_length=10)

    class Meta:
        db_table = "Login"
