from django.db import models

class Alert(models.Model):
    message = models.CharField(max_length=200)

    messages = models.ManyToManyField('self', related_name='messages')
