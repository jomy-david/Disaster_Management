from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    camp_id = models.CharField(max_length=3)
    contact = models.CharField(max_length=10)
    gender = models.CharField(max_length=7)