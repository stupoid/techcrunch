from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Shelter(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField()
    hq_id = models.IntegerField()
    need_water = models.BooleanField()
    occupancy = models.IntegerField()
    max_occupancy = models.IntegerField()

class Routes(models.Model):
    user_id = models.IntegerField()
    from_shelter = models.IntegerField()
    to_shelter = models.IntegerField()
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    arrival_confirmed = models.BooleanField()

class CheckIn(models.Model):
    user_id = models.IntegerField()
    shelter_id = models.IntegerField()
    timestamp = models.DateTimeField()

class User(models.Model):
    user_id = models.IntegerField()
    end_shelter = models.IntegerField()
    last_shelter = models.IntegerField()
    name = models.CharField()
    able_bodied = models.BooleanField()