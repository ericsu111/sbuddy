# Generated by Django 3.1.1 on 2020-11-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbuddy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
    ]