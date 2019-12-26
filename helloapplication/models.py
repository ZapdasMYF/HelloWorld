from django.db import models
from datetime import date,time,datetime
from django.utils import timezone



# Create your models here.
#from django.utils.timezone.now from datetime

class Data(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password =models.CharField(max_length=200)


class Feedbackpost(models.Model):
    index=models.AutoField(primary_key=True)
    txtfield = models.CharField(max_length=500)
    date = models.DateField(default=date.today(), blank=True)

    now = timezone.now()

    current_time = now.strftime("%H:%M:%S")
    time = models.TimeField(default=current_time, blank=True)

    def __str__(self):
        return 'Post:' + self.txtfield + ' Index :' + str(self.index) + ' '
