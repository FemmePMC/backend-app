from django.db import models
from user.models import User

class Alert(models.Model):
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alert_user')
    messages = models.ManyToManyField('self', related_name='messages')
