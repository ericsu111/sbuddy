# Generated by Django 3.1.3 on 2020-11-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbuddy', '0010_auto_20201115_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.PositiveIntegerField()),
            ],
        ),
    ]