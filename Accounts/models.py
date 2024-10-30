from django.db import models

# Create your models here.
class Customer_register(models.Model):
    name= models.CharField(max_length=100)
    mobile = models.BigIntegerField(unique=True)
    email = models.CharField(unique=True)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)


class Passenger_register(models.Model):
    name= models.CharField(max_length=100)
    mobile = models.BigIntegerField(unique=True)
    email = models.CharField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    