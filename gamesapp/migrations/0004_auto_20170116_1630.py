# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 16:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesapp', '0003_auto_20170116_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 16, 16, 30, 50, 112136)),
        ),
        migrations.AlterField(
            model_name='highscore',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 16, 16, 30, 50, 112636)),
        ),
    ]
