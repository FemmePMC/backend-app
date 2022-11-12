from django.db import models
from femme_back.user.models import User

class Location(models.model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    zone = models.CharField(max_length=50)
