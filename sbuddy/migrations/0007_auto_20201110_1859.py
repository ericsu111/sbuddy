# Generated by Django 3.1.1 on 2020-11-10 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbuddy', '0006_auto_20201110_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='availability',
            field=models.CharField(choices=[('Monday Morning', 'Monday Morning'), ('Monday Afternoon', 'Monday Afternoon'), ('Tuesday Morning', 'Tuesday Morning'), ('Tuesday Afternoon', 'Tuesday Afternoon'), ('Wednesday Morning', 'Wednesday Morning'), ('Wednesday Afternoon', 'Wednesday Afternoon'), ('Thursday Morning', 'Thursday Morning'), ('Thursday Afternoon', 'Thursday Afternoon'), ('Friday Morning', 'Friday Morning'), ('Friday Afternoon', 'Friday Afternoon')], default='Monday Morning', max_length=50),
        ),
    ]