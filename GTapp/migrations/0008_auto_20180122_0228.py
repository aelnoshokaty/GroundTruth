# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-22 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GTapp', '0007_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_request_sent', models.BooleanField(default=False)),
                ('has_extended_profile', models.BooleanField(default=False)),
                ('profile_use_background_image', models.BooleanField(default=False)),
                ('contributors_enabled', models.BooleanField(default=False)),
                ('live_following', models.BooleanField(default=False)),
                ('translator_type', models.CharField(default='', max_length=250)),
                ('verified', models.BooleanField(default=False)),
                ('blocked_by', models.BooleanField(default=False)),
                ('profile_text_color', models.CharField(default='', max_length=250)),
                ('muting', models.BooleanField(default=False)),
                ('profile_image_url_https', models.CharField(default='', max_length=250)),
                ('profile_sidebar_fill_color', models.CharField(default='', max_length=250)),
                ('followers_count', models.IntegerField(default=-1)),
                ('profile_sidebar_border_color', models.CharField(default='', max_length=250)),
                ('id_str', models.CharField(default='', max_length=250)),
                ('default_profile_image', models.BooleanField(default=False)),
                ('ChangeFollower', models.CharField(default='', max_length=250)),
                ('listed_count', models.IntegerField(default=-1)),
                ('is_translation_enabled', models.BooleanField(default=False)),
                ('utc_offset', models.IntegerField(default=-1)),
                ('statuses_count', models.IntegerField(default=-1)),
                ('description', models.CharField(default='', max_length=250)),
                ('friends_count', models.IntegerField(default=-1)),
                ('location', models.CharField(default='', max_length=250)),
                ('profile_link_color', models.CharField(default='', max_length=250)),
                ('profile_image_url', models.CharField(default='', max_length=250)),
                ('notifications', models.BooleanField(default=False)),
                ('geo_enabled', models.BooleanField(default=False)),
                ('profile_background_color', models.CharField(default='', max_length=250)),
                ('blocking', models.BooleanField(default=False)),
                ('profile_background_image_url', models.CharField(default='', max_length=250)),
                ('screen_name', models.CharField(default='', max_length=250)),
                ('lang', models.CharField(default='', max_length=250)),
                ('following', models.BooleanField(default=False)),
                ('profile_background_tile', models.BooleanField(default=False)),
                ('favourites_count', models.IntegerField(default=-1)),
                ('name', models.CharField(default='', max_length=250)),
                ('url', models.CharField(default='', max_length=250)),
                ('CollectedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.CharField(default='', max_length=250)),
                ('profile_background_image_url_https', models.CharField(default='', max_length=250)),
                ('time_zone', models.CharField(default='', max_length=250)),
                ('protected', models.BooleanField(default=False)),
                ('default_profile', models.BooleanField(default=False)),
                ('is_translator', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-screen_name',),
            },
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='ChangeFollower',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='CollectedTimeStamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='blocked_by',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='blocking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='contributors_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='created_at',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='default_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='default_profile_image',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='favourites_count',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='follow_request_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='followers_count',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='following',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='friends_count',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='geo_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='has_extended_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='is_translation_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='is_translator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='lang',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='listed_count',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='live_following',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='location',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='muting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='notifications',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_background_color',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_background_image_url',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_background_image_url_https',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_background_tile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_image_url',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_image_url_https',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_link_color',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_sidebar_border_color',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_sidebar_fill_color',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_text_color',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_use_background_image',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='protected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='statuses_count',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='time_zone',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='translator_type',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='url',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='utc_offset',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='id_str',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='screen_name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='twitterfriend',
            name='twitterUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='GTapp.TwitterUser'),
        ),
    ]
