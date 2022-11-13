from django.db import models

class Alert(moedls.Model):
    message = models.CharField(max_length=200)

    messages = models.ManyToManyField(Message, related_name='messages')
