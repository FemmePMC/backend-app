# Generated by Django 3.2.6 on 2022-11-13 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('alert', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField()),
                ('id_type', models.CharField(max_length=2)),
                ('nickname', models.CharField(max_length=20)),
                ('pasword', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('photo', models.ImageField(blank=True, upload_to='user_photos')),
                ('height', models.FloatField()),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('alerts_received', models.ManyToManyField(related_name='alerts_received', to='alert.Alert')),
                ('emergency_contacts', models.ManyToManyField(related_name='_user_user_emergency_contacts_+', to='user.User')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='location.location')),
            ],
        ),
        migrations.DeleteModel(
            name='Nombre',
        ),
    ]
