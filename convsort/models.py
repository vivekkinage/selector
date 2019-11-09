from django.db import models
import datetime


class REGISTRATIONS(models.Model):
    user_key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100,default="something")
    phone = models.CharField(max_length=100)

class job(models.Model):
    date=models.DateField(default=datetime.datetime.now())
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=600)
    skills=models.CharField(max_length=10000)

class cvs(models.Model):
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    status=models.BooleanField(default=0)
    path=models.CharField(max_length=600)
    uid=models.IntegerField()
    jid=models.IntegerField()
    skills=models.CharField(max_length=10000)
