# Generated by Django 3.1.1 on 2020-11-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbuddy', '0004_auto_20201119_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]