from django.db import models
from Accounts.models import Passenger_register

# Create your models here.
class Trains(models.Model):
    train_no = models.IntegerField(unique=True)
    train_name = models.CharField()
    from_station = models.CharField(max_length=100)
    to_station = models.CharField(max_length=100)
    coaches = models.IntegerField()
    seats = models.IntegerField()
    train_type = models.CharField(max_length=100)
    running_days = models.CharField(default='W-T-F')


class Stations(models.Model):
    station_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class Platforms(models.Model):
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    platform_no = models.IntegerField()
    train_time = models.CharField()
    train_name = models.ForeignKey(Trains, on_delete=models.CASCADE)

class Booking(models.Model):
    passenger = models.ForeignKey(Passenger_register, on_delete=models.CASCADE)
    pnr = models.BigIntegerField()
    train = models.ForeignKey(Trains, on_delete= models.CASCADE)
    seat_no = models.CharField()
    booking_date = models.DateTimeField()
    status = models.CharField()
    waiting_no = models.IntegerField()
    from_station = models.CharField(max_length=100)
    to_station = models.CharField(max_length=100)
    booking_time = models.DateTimeField(auto_now=True)

class Train_fare(models.Model):
    train_name = models.ForeignKey(Trains, on_delete=models.CASCADE)
    from_station = models.ForeignKey(Stations, related_name='from_station' , on_delete=models.CASCADE)
    to_station = models.ForeignKey(Stations, related_name='to_station', on_delete=models.CASCADE)
    amount = models.FloatField()

class Payment(models.Model):
    train_amount = models.ForeignKey(Train_fare, on_delete=models.CASCADE)
    razorpay_id = models.BigIntegerField()

class Cancellation(models.Model):
    time = models.DateTimeField()
    refund_amount = models.FloatField()
    deduction = models.FloatField()
    train_amount = models.ForeignKey(Train_fare, on_delete=models.CASCADE)
    booking_data = models.ForeignKey(Booking, on_delete=models.CASCADE)  


class Chart(models.Model):
    booking_info = models.ForeignKey(Booking, on_delete=models.CASCADE)