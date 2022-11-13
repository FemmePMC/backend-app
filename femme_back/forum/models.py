from django.db import models
from user.models import User

# Create your models here.

class Forum(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tema = models.CharField(max_length=50)

    users = models.ManyToManyField('self', related_name='users')