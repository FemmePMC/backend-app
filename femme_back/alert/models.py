from django.db import models

class Alert(models.Model):
    message = models.CharField(max_length=200)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name='alert_user')
    messages = models.ManyToManyField('self', related_name='messages')
