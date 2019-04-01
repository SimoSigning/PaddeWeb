# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaddeApp', '0002_userprofile_skildpadde'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteTurtle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('turtleinfo', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
