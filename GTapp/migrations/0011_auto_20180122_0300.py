# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-22 03:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GTapp', '0010_auto_20180122_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='petition',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='twitterUser',
        ),
        migrations.RemoveField(
            model_name='tweets',
            name='twitterUser',
        ),
        migrations.RemoveField(
            model_name='twitterfriend',
            name='twitterUser',
        ),
        migrations.DeleteModel(
            name='Petition',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
        migrations.DeleteModel(
            name='Tweets',
        ),
        migrations.DeleteModel(
            name='TwitterFriend',
        ),
        migrations.DeleteModel(
            name='TwitterUser',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]