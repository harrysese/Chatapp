# Generated by Django 5.0.4 on 2024-04-11 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.IntegerField(blank=True, default=datetime.datetime(2024, 4, 11, 21, 8, 53, 898133)),
        ),
    ]