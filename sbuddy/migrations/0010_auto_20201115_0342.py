# Generated by Django 3.1.3 on 2020-11-15 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbuddy', '0009_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
