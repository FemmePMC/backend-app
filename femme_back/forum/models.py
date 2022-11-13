from django.db import models

# Create your models here.

class Forum(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tema = models.CharField(max_length=50)

    forum = models.ManyToManyField('self', related_name='forum')
