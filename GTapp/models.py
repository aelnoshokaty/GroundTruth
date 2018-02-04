from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User


class Petition(models.Model):
    petition_id = models.IntegerField()
    title = models.CharField(max_length=2000)
    url = models.CharField(max_length=200)


class TwitterUser(models.Model):
    follow_request_sent = models.BooleanField(default=False)
    has_extended_profile = models.BooleanField(default=False)
    profile_use_background_image = models.BooleanField(default=False)
    contributors_enabled = models.BooleanField(default=False)
    live_following = models.BooleanField(default=False)
    translator_type = models.CharField(max_length=250, default='')
    verified = models.BooleanField(default=False)
    blocked_by = models.BooleanField(default=False)
    profile_text_color = models.CharField(max_length=250, default='')
    muting = models.BooleanField(default=False)
    profile_image_url_https = models.CharField(max_length=250, default='')
    profile_sidebar_fill_color = models.CharField(max_length=250, default='')
    followers_count = models.IntegerField(default=-1)
    profile_sidebar_border_color = models.CharField(max_length=250, default='')
    id_str = models.CharField(max_length=250, default='')
    default_profile_image = models.BooleanField(default=False)
    ChangeFollower = models.CharField(max_length=250, default='')
    listed_count = models.IntegerField(default=-1)
    is_translation_enabled = models.BooleanField(default=False)
    utc_offset = models.IntegerField(default=-1)
    statuses_count = models.IntegerField(default=-1)
    description = models.CharField(max_length=250, default='')
    friends_count = models.IntegerField(default=-1)
    location = models.CharField(max_length=250, default='')
    profile_link_color = models.CharField(max_length=250, default='')
    profile_image_url = models.CharField(max_length=250, default='')
    notifications = models.BooleanField(default=False)
    geo_enabled = models.BooleanField(default=False)
    profile_background_color = models.CharField(max_length=250, default='')
    blocking = models.BooleanField(default=False)
    profile_background_image_url = models.CharField(max_length=250, default='')
    screen_name = models.CharField(max_length=250, default='')
    lang = models.CharField(max_length=250, default='')
    following = models.BooleanField(default=False)
    profile_background_tile = models.BooleanField(default=False)
    favourites_count = models.IntegerField(default=-1)
    name = models.CharField(max_length=250, default='')
    url = models.CharField(max_length=250, default='')
    CollectedTimeStamp = models.DateTimeField(default=timezone.now)
    created_at = models.CharField(max_length=250, default='')
    profile_background_image_url_https = models.CharField(max_length=250, default='')
    time_zone = models.CharField(max_length=250, default='')
    protected = models.BooleanField(default=False)
    default_profile = models.BooleanField(default=False)
    is_translator = models.BooleanField(default=False)
    class Meta:
        ordering = ('-screen_name',)

    def __str__(self):
        return self.screen_name


class Ratings (models.Model):
    twitterUser = models.CharField(max_length=250)
    petition = models.CharField(max_length=250)
    rating = models.IntegerField()

class Tweets(models.Model):
   collected_at = models.DateTimeField(default=timezone.now)
   user_id = models.CharField(max_length=250)
   created_at = models.DateTimeField
   id_str = models.CharField(max_length=250)
   text = models.CharField(max_length=250)
   source = models.CharField(max_length=250, default='')
   truncated = models.BooleanField(default=False)
   in_reply_to_status_id_str = models.CharField(max_length=250, default='')
   in_reply_to_user_id_str = models.CharField(max_length=250, default='')
   in_reply_to_screen_name = models.CharField(max_length=250, default='')
   coordinatesNumber = models.IntegerField(default=-1)
   coordinates = models.CharField(max_length=250, default='')
   coordinatesType = models.CharField(max_length=250, default='')
   placeCountry = models.CharField(max_length=250, default='')
   placeCountryCode = models.CharField(max_length=250, default='')
   placeFullName = models.CharField(max_length=250, default='')
   placeID = models.CharField(max_length=250, default='')
   placeName = models.CharField(max_length=250, default='')
   placeType = models.CharField(max_length=250, default='')
   placeURL = models.CharField(max_length=250, default='')
   quoted_status_id_str= models.CharField(max_length=250, default='')
   is_quote_status = models.BooleanField(default=False)
   retweeted_status = models.CharField(max_length=250, default='')
   quote_count = models.IntegerField(default=-1)
   reply_count = models.IntegerField(default=-1)
   retweet_count = models.IntegerField(default=-1)
   favorite_count = models.IntegerField(default=-1)
   hashtagsNumber = models.IntegerField(default=-1)
   hashtags = models.CharField(max_length=250, default='')
   urls = models.CharField(max_length=250, default='')
   urlsNumber = models.IntegerField(default=-1)
   user_mentionsNumber = models.IntegerField()
   user_mentions = models.CharField(max_length=250, default='')
   mediaNumber = models.IntegerField(default=-1)
   mediaURLs = models.CharField(max_length=250, default='')
   mediaType = models.CharField(max_length=250, default='')
   symbolsNumber = models.CharField(max_length=250, default='')
   symbols = models.CharField(max_length=250, default='')
   pollsNumber = models.IntegerField(default=-1)
   polls = models.CharField(max_length=250, default='')
   possibly_sensitive = models.BooleanField(default=False)
   filter_level = models.CharField(max_length=250, default='')
   lang = models.CharField(max_length=250, default='')
   matching_rulesNumber = models.IntegerField(default=-1)
   matching_rulesTag = models.CharField(max_length=250, default='')
   matching_rulesID = models.CharField(max_length=250, default='')
   class Meta:
       ordering = ('collected_at',)
   def __str__(self):
       return '{} tweeted by {}'.format(self.text, self.user_id)