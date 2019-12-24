from django.db import models

# Create your models here.

class Data(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password =models.CharField(max_length=200)
