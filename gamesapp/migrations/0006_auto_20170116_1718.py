# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 17:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamesapp', '0005_auto_20170116_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ('date_added',)},
        ),
        migrations.AlterModelOptions(
            name='highscore',
            options={'ordering': ('date_added',)},
        ),
    ]