from django.db import models
from femme_back.location.models import Location
from femme_back.forum.models import Forum
from femme_back.alert.models import Alert

# Create your models here.

class User(models.Model):
    id_number = models.IntegerField()
    id_type = models.CharField(max_length=2)
    nickname = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    pasword = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='user_photos', blank=True)
    height = models.FloatField()

    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    forums = models.ManyToManyField(Forum)
    alerts_received = models.ManyToManyField(Alert, related_name='alerts_received')
    emergency_contacts = models.ManyToManyField('self', related_name='emergency_contacts')
    