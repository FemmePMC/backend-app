from django.db import models
from location.models import Location
from alert.models import Alert

# Create your models here.

class User(models.Model):
    id_number = models.IntegerField()
    id_type = models.CharField(max_length=2)
    nickname = models.CharField(max_length=20)
    pasword = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='user_photos', blank=True)
    height = models.FloatField()

    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    alerts_received = models.ManyToManyField(Alert, related_name='alerts_received')
    emergency_contacts = models.ManyToManyField('self', related_name='emergency_contacts')
    