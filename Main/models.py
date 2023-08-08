from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    camp_id = models.CharField(max_length=3)
    contact = models.CharField(max_length=10)
    gender = models.CharField(max_length=7)

class Camp(models.Model):
    camp_id = models.CharField(max_length=3,unique=True)
    camp_name = models.CharField(max_length=20)
    camp_add = models.CharField(max_length=60)
    camp_district = models.CharField(max_length=20)
    camp_state = models.CharField(max_length=20)
    camp_man = models.CharField(max_length=20) 
    man_id = models.CharField(max_length=5,unique=True)
    camp_img = models.ImageField(upload_to="Camp_Images")
    man_contact = models.IntegerField()
    curr_capacity = models.PositiveIntegerField()
    total_capacity = models.PositiveIntegerField()
    rat_towel = models.PositiveIntegerField()
    rat_soap = models.PositiveIntegerField()


