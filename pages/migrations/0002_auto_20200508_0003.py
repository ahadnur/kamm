# Generated by Django 3.0.5 on 2020-05-07 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
