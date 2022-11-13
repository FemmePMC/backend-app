# Generated by Django 3.2.6 on 2022-11-13 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('messages', models.ManyToManyField(related_name='_alert_alert_messages_+', to='alert.Alert')),
            ],
        ),
    ]
