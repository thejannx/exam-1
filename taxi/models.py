from django.db import models


class Taxi(models.Model):
    taxi_name = models.CharField(max_length=25)
    license_plate = models.CharField(max_length=15)
    driver_name = models.CharField(max_length=50)
    passenger_capacity = models.IntegerField()
    car_model = models.CharField(max_length=20)
    is_completed = models.BooleanField(default=False)
