from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Shelter(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=255, null=True)
    hq_id = models.IntegerField(null=True)
    need_water = models.BooleanField(default=True)
    occupancy = models.IntegerField(null=True)
    max_occupancy = models.IntegerField(null=True)
    ready_to_accommodate = models.BooleanField(default=True)
    power_status = models.BooleanField(default=True)
    water_status = models.BooleanField(default=True)
    connectivity_status = models.BooleanField(default=True)

class Routes(models.Model):
    user_id = models.IntegerField(null=True)
    from_shelter = models.IntegerField(null=True)
    to_shelter = models.IntegerField(null=True)
    departure_time = models.DateTimeField(null=True)
    arrival_time = models.DateTimeField(null=True)
    arrival_confirmed = models.BooleanField(default=True)

class CheckIn(models.Model):
    user_id = models.IntegerField(null=True)
    shelter_id = models.IntegerField(null=True)
    timestamp = models.DateTimeField(null=True)

class User(models.Model):
    user_id = models.IntegerField(null=True)
    end_shelter = models.IntegerField(null=True)
    last_shelter = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    able_bodied = models.BooleanField(default=True)
    contact_number = models.IntegerField(null=True)
    