# Generated by Django 3.2.6 on 2022-11-21 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_pasword_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.CharField(max_length=120),
        ),
    ]
