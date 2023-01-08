from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class Template(models.Model):
    name = models.TextField(max_length=63, unique=True)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True)
    date = models.DateField()
    text = models.CharField(max_length=270)
