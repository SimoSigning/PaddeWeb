# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 16:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PaddeApp', '0005_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='likes_turtles',
        ),
    ]