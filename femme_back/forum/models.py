from django.db import models
from user.models import User

# Create your models here.

class Forum(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tema = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    users = models.ManyToManyField(User, related_name='users')