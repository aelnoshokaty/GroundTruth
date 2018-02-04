# Django
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, render, redirect
from django.core.urlresolvers import reverse

# Project
#from mytwitterapp.models import Profile
#from models import Petition, TwitterUser, TwitterFriends, Ratings, Tweets
#from models import Petition, TwitterUser, TwitterFriends, Ratings, Tweets
import helloworld.settings as settings

# Python
import oauth2 as oauth
#import urlparse
import cgi
#import threading
#import signal
#import time
import sqlite3
from random import randint
import tweepy
import oauth2
#import signal
#import httplib
import time
#import oauth.oauth as oauthc
#import ast
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#from socket import *
#import SimpleHTTPServer
#import SocketServer
import json
#import datetime
from time import gmtime, strftime



twitter_handle='change'

# It's probably a good idea to put your consumer's OAuth token and
# OAuth secret into your project's settings.
consumer = oauth.Consumer(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
client = oauth.Client(consumer)

auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
api = tweepy.API(auth,retry_count=3, retry_delay=60,retry_errors=set([401, 404, 500, 503]),wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'

# This is the slightly different URL used to authenticate/authorize.
authenticate_url = 'https://api.twitter.com/oauth/authenticate'
REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
CALLBACK_URL = 'http://localhost:8000/display_petitions'





def getRandomPetitions(l):
    db_file = "/home/ubuntu/GTapp-virtualenv/helloworld/db.sqlite3"
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    cursor = conn.cursor()
    data = cursor.execute('''SELECT * From GTapp_petition''')
    data1 = data.fetchall()
    petitionID = []
    petitionURL = []
    petitionTitle = []
    total = 0
    for it in data1:
        petitionID.append(it[1])
        petitionTitle.append(it[2])
        petitionURL.append(it[3])
        total+=1
    count = 0
    petitionsSet = {}
    petitionsSet = set()
    while count < l:
        i = randint(0, total-1)
        if not petitionID[i] in petitionsSet:
            petitionsSet.add(i)
            count += 1

    count=0
    petitionIDRand=[]
    petitionURLRand = []
    petitionTitleRand = []
    for i in petitionsSet:
        petitionIDRand.append(petitionID[i])
        petitionURLRand.append(petitionURL[i])
        petitionTitleRand.append(petitionTitle[i])
    petitionCollection =[]
    petitionCollection.append(petitionIDRand)
    petitionCollection.append(petitionURLRand)
    petitionCollection.append(petitionTitleRand)
    return petitionCollection


def delete_user(userid):
    return

def sqlite_insert(conn, table, row):
    cols = ', '.join('"{}"'.format(col) for col in row.keys())
    vals = ', '.join(':{}'.format(col) for col in row.keys())
    sql = 'INSERT INTO "{0}" ({1}) VALUES ({2})'.format(table, cols, vals)
    conn.cursor().execute(sql, row)
    conn.commit()

def insert_user(usrObj):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    db_file = "/home/ubuntu/GTapp-virtualenv/helloworld/db.sqlite3"
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    collected=strftime("%Y-%m-%d %H:%M:%S", gmtime())
    col=["id_str", "follow_request_sent", "has_extended_profile", "profile_use_background_image", "contributors_enabled", "live_following", "translator_type", "verified", "blocked_by", "profile_text_color", "muting", "profile_image_url_https", "profile_sidebar_fill_color", "followers_count", "profile_sidebar_border_color", "default_profile_image", "ChangeFollower", "listed_count", "is_translation_enabled", "utc_offset", "statuses_count", "description", "friends_count", "location", "profile_link_color", "profile_image_url", "notifications", "geo_enabled", "profile_background_color", "blocking", "profile_background_image_url", "screen_name", "lang", "following", "profile_background_tile", "favourites_count", "name", "url", "CollectedTimeStamp", "created_at", "profile_background_image_url_https", "time_zone", "protected", "default_profile", "is_translator"]

    userdb={}
    for key, value in usrObj.iteritems():
        if key in col:
            userdb[key]=usrObj[key]
    userdb["CollectedTimeStamp"]=collected
    sqlite_insert(conn,'GTapp_twitteruser',userdb)



def delete_tweets(userid):
    return


def insert_tweets(post):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    db_file = "/home/ubuntu/GTapp-virtualenv/helloworld/db.sqlite3"
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    for i in range(0,len(post['id_str'])):
        tweet={}
        tweet['user_id']=post['user_id']
        tweet['created_at'] = post['created_at'][i]
        tweet['id_str'] = post['id_str'][i]
        tweet['text'] = post['text'][i]
        tweet['source'] = post['source'][i]
        tweet['truncated'] = post['truncated'][i]
        tweet['in_reply_to_status_id_str'] = post['in_reply_to_status_id_str'][i]
        tweet['in_reply_to_screen_name'] = post['in_reply_to_screen_name'][i]
        tweet['coordinatesNumber'] = post['coordinatesNumber'][i]
        tweet['coordinates'] = post['coordinates'][i]
        tweet['coordinatesType'] = post['coordinatesType'][i]
        tweet['placeCountry'] = post['placeCountry'][i]
        tweet['placeCountryCode'] = post['placeCountryCode'][i]
        tweet['placeFullName'] = post['placeFullName'][i]
        tweet['placeID'] = post['placeID'][i]
        tweet['placeName'] = post['placeName'][i]
        tweet['placeType'] = post['placeType'][i]
        tweet['placeURL'] = post['placeURL'][i]
        tweet['quoted_status_id_str'] = post['quoted_status_id_str'][i]
        tweet['is_quote_status'] = post['is_quote_status'][i]
        tweet['retweeted_status'] = post['retweeted_status'][i]
        tweet['quote_count'] = post['quote_count'][i]
        tweet['reply_count'] = post['reply_count'][i]
        tweet['retweet_count'] = post['retweet_count'][i]
        tweet['favorite_count'] = post['favorite_count'][i]
        tweet['hashtagsNumber'] = post['hashtagsNumber'][i]
        tweet['hashtags'] = post['hashtags'][i]
        tweet['urls'] = post['urls'][i]
        tweet['urlsNumber'] = post['urlsNumber'][i]
        tweet['user_mentionsNumber'] = post['user_mentionsNumber'][i]
        tweet['user_mentions'] = post['user_mentions'][i]
        tweet['mediaNumber'] = post['mediaNumber'][i]
        tweet['mediaURLs'] = post['mediaURLs'][i]
        tweet['mediaType'] = post['mediaType'][i]
        tweet['symbolsNumber'] = post['symbolsNumber'][i]
        tweet['symbols'] = post['symbols'][i]
        tweet['pollsNumber'] = post['pollsNumber'][i]
        tweet['polls'] = post['polls'][i]
        tweet['possibly_sensitive'] = post['possibly_sensitive'][i]
        tweet['filter_level'] = post['filter_level'][i]
        tweet['lang'] = post['lang'][i]
        tweet['matching_rulesNumber'] = post['matching_rulesNumber'][i]
        tweet['matching_rulesTag'] = post['matching_rulesTag'][i]
        tweet['matching_rulesID'] = post['matching_rulesID'][i]
        tweet['collected_at'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        sqlite_insert(conn, 'GTapp_tweets', tweet)


def pause():
    print('')
    time.sleep(1)

def insert_ratings(uid,petitionsIDs,petitionsValues):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """

    ratings=[]
    for i in range(0, len(petitionsValues)):
        ls = []
        ls.append(petitionsValues[i])
        ls.append(petitionsIDs[i])
        ls.append(uid)
        ratings.append(tuple(ls))
    db_file = "/home/ubuntu/GTapp-virtualenv/helloworld/db.sqlite3"
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    cur = conn.cursor()
    cur.executemany('insert into GTapp_ratings(rating,petition_id,user_id) values (?,?,?)', ratings)
    conn.commit()
    #cur.execute(sql, petition)
    #return cur.lastrowid

def pause():
    print('')
    time.sleep(1)


'''
def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', 'abcdefg', 'hijklmnop' )
'''


def parseAmp(s):
    l=[]
    temp=""
    flag=False
    for i in s:
        if i =='&':
            l.append(temp)
            temp=""
            flag=False
        if flag:
            temp += i
        if i =='=':
            flag=True
    return l


def twitter_login(request):
    print consumer
    print client
    # Step 1. Get a request token from Twitter.
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response from Twitter.")


    l=parseAmp(content)
    #par = urlparse.parse_qs(urlparse.urlparse(content).query)



    # Step 2. Store the request token in a session for later use.
    request.session['request_token_oauth_token'] = l[0]
    print ''
    print request.session['request_token_oauth_token']
    request.session['request_token_oauth_token_secret'] = l[1]

    # Step 3. Redirect the user to the authentication URL.
    #url = "%s?oauth_token=%s" % (authenticate_url,
        #request.session['request_token']['oauth_token'])
    url = "%s?oauth_token=%s" % (authenticate_url,
                                 request.session['request_token_oauth_token'])
    return HttpResponseRedirect(url)


@login_required
def twitter_logout(request):
    # Log a user out using Django's logout function and redirect them
    # back to the homepage.
    logout(request)
    return HttpResponseRedirect('/')

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=settings.CONSUMER_KEY, secret=settings.CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content


def get_all_tweets(uid):
    # Twitter only allows access to a users most recent 3240 tweets with this method
    tweets_str=''
    # initialize a list to hold all the tweepy Tweets
    alltweets = []
    outtweets = {}
    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(id=uid, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    count=0
    #while len(new_tweets) > 0:

    # Get 1600 tweets to user
    while count<17:
        print "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(id=uid, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))
        count+=1

    # transform the tweepy tweets into a 2D array that will populate in database

    tweetsCreated_at=[]

    tweetsID = []
    tweetsIDStr = []
    tweetsText = []
    tweetsSource = []
    tweetsTruncated = [] #indicates if the tweet was trimmed usually from cross social media platform

    tweetsIn_reply_to_status_id_str = []
    tweetsIn_reply_to_user_id_str = []
    tweetsIn_reply_to_screen_name = []

    #tweetsContributors = []
    tweetsCoordinatesNumber = []
    tweetsCoordinates = []
    tweetsCoordinatesType = []

    tweetsPlaceCountryCode=[]
    tweetsPlaceCountry=[]
    tweetsPlaceFullName = []
    tweetsPlaceID=[]
    tweetsPlaceName=[]
    tweetsPlaceType = []
    tweetsPlaceURL=[]

    tweet_Quoted_status_id_str = []
    tweetsIs_quote_status = []
    tweetsQuote_status = []

    tweetsRetweet_status = []

    tweetsQuote_count = []

    tweetsReply_count = []

    tweetsRetweet_count = []


    #Entity object
    tweetsHashtagsNumber = []
    tweetsHashtags=[]
    tweetsMediaNumber = []
    tweetsMediaType =[]
    tweetsMediaURLs = []
    tweetsURLsNumber = []
    tweetsURLs =[]
    tweetsMentionsNumber = []
    tweetsMentions = []
    tweetsSymbols = []
    tweetsSymbolsNumber = []   # presence of $ or any symbol
    tweetsPolls = []
    tweetsPollsNumber = []

    tweetsFavorite_count = []
    tweetsFavorited = []
    tweetsRetweeted = []
    tweetsPossibly_sensitive = []  #Contains link
    tweetsFiltered_level = []  #Streaming option
    tweetsLang = []

    #Matching Rule object
    tweetsMatching_rulesNumber = []
    tweetsMatching_rulesTag = []
    tweetsMatching_rulesID = []

    for tweet in alltweets:
        #outtweets['id']=tweet.id_str
        #outtweets['details']=[tweet.created_at,tweet.text.encode("utf-8")]
        #tweets_str=tweets_str+'. '+tweet.text.encode("utf-8")
        #tweetsList.append(outtweets)

        tweetsCreated_at.append(tweet.created_at)
        #tweetsContributors.append(tweet.contributors)

        tweetsID.append(tweet.id)
        tweetsIDStr.append(tweet.id_str)
        tweetsText.append(tweet.text)
        tweetsSource.append(tweet.source)
        tweetsTruncated.append(tweet.truncated)
        tweetsIn_reply_to_status_id_str.append(tweet.in_reply_to_status_id_str)
        tweetsIn_reply_to_user_id_str.append(tweet.in_reply_to_user_id_str)
        tweetsIn_reply_to_screen_name.append(tweet.in_reply_to_screen_name)
        coordNumber=0
        coord=""
        coordType=""
        if hasattr(tweet, 'coordinates'):
            if tweet.coordinates is not None:
                if tweet.coordinates["coordinates"]:
                    coordNumber = len(tweet.coordinates["coordinates"])
                    if tweet.coordinates["coordinates"]:
                        for coordi in tweet.coordinates["coordinates"]:
                            coord = " "+coord + "," + str(coordi).encode("utf-8")
                if tweet.coordinates["type"]:
                    coordType = tweet.coordinates["type"].encode("utf-8")
        tweetsCoordinatesNumber.append(coordNumber)
        tweetsCoordinates.append(coord)
        tweetsCoordinatesType.append(coordType)

        placeCountry=""
        placeCountryCode=""
        placeFullName = ""
        placeID= ""
        placeName=""
        placeType=""
        placeURL=""
        if hasattr(tweet, 'place'):
            if tweet.place is not None:
                if tweet.place.country:
                    placeCountry=tweet.place.country.encode("utf-8")
                if tweet.place.country_code:
                    placeCountryCode=tweet.place.country_code.encode("utf-8")
                if tweet.place.full_name:
                    placeFullName=tweet.place.full_name.encode("utf-8")
                if tweet.place.id:
                    placeID=tweet.place.id.encode("utf-8")
                if tweet.place.name:
                    placeName=tweet.place.name.encode("utf-8")
                if tweet.place.place_type:
                    placeType=tweet.place.place_type.encode("utf-8")
                if tweet.place.url:
                    placeURL=tweet.place.url.encode("utf-8")

        tweetsPlaceCountry.append(placeCountry)
        tweetsPlaceCountryCode.append(placeCountryCode)
        tweetsPlaceFullName.append(placeFullName)
        tweetsPlaceID.append(placeID)
        tweetsPlaceName.append(placeName)
        tweetsPlaceType.append(placeType)
        tweetsPlaceURL.append(placeURL)

        tweetsIs_quote_status.append(tweet.is_quote_status)
        if tweet.is_quote_status == True:
            if hasattr(tweet, 'quoted_status_id_str'):
                tweetsQuote_status.append(tweet.quoted_status_id_str)
            else:
                tweetsQuote_status.append("")
        else:
            tweetsQuote_status.append("")


        if hasattr(tweet, 'retweeted_status'):
            if tweet.retweeted_status is not None:
                tweetsRetweet_status.append(tweet.retweeted_status.id_str)
            else:
                tweetsRetweet_status.append("")
        else:
            tweetsRetweet_status.append("")


        if hasattr(tweet, 'quote_count'):
            if tweet.quote_count is not None:
                tweetsQuote_count.append(tweet.quote_count)
            else:
                tweetsQuote_count.append(0)
        else:
            tweetsQuote_count.append(0)

        if hasattr(tweet, 'reply_count'):
            if tweet.reply_count is not None:
                tweetsReply_count.append(tweet.reply_count)
            else:
                tweetsReply_count.append(0)
        else:
            tweetsReply_count.append(0)

        if hasattr(tweet, 'retweet_count'):
            if tweet.retweet_count is not None:
                tweetsRetweet_count.append(tweet.retweet_count)
            else:
                tweetsRetweet_count.append(0)
        else:
            tweetsRetweet_count.append(0)

        if hasattr(tweet, 'favorite_count'):
            if tweet.favorite_count is not None:
                tweetsFavorite_count.append(tweet.favorite_count)
            else:
                tweetsFavorite_count.append(0)
        else:
            tweetsFavorite_count.append(0)

        htNumber=0
        ht=""
        mediaNumber = 0
        mediaType = ""
        mediaURL = ""
        URLNumber = 0
        urlstr = ""
        umNumber = 0
        um = ""
        symNumber = 0
        sym = ""
        pollNumber = 0
        poll = ""
        if hasattr(tweet, 'entities'):
            if 'hashtags' in tweet.entities:
            #if hasattr(tweet.entities, 'hashtags'):
                htNumber = len(tweet.entities["hashtags"])
                if tweet.entities["hashtags"]:
                    for hti in tweet.entities["hashtags"]:
                        if 'text' in hti:
                            ht = ht + " " + hti["text"].encode("utf-8")
            if 'media' in tweet.entities:
                mediaNumber = len(tweet.entities["media"])
                if tweet.entities["media"]:
                    for medi in tweet.entities["media"]:
                        if 'type' in medi:
                            mediaType = mediaType + " " + medi["type"].encode("utf-8")
                        if 'media_url' in medi:
                            mediaURL = mediaURL + " " + medi["media_url"].encode("utf-8")

            if 'urls' in tweet.entities:
                URLNumber = len(tweet.entities["urls"])
                if tweet.entities["urls"]:
                    for URLi in tweet.entities["urls"]:
                        if 'url' in URLi:
                            urlstr = urlstr + " " + URLi["url"].encode("utf-8")

            if 'user_mentions' in tweet.entities:
                umNumber = len(tweet.entities["user_mentions"])
                if tweet.entities["user_mentions"]:
                    for umi in tweet.entities["user_mentions"]:
                        if 'id_str' in umi:
                            um = um + " " + umi["id_str"]

            if 'symbols' in tweet.entities:
                symNumber = len(tweet.entities["symbols"])
                if tweet.entities["symbols"]:
                    for symi in tweet.entities["symbols"]:
                        if 'text' in symi:
                            sym = sym+" "+symi["text"].encode("utf-8")


            if 'polls' in tweet.entities:
                symNumber = len(tweet.entities["polls"])
                if tweet.entities["polls"]:
                    for polli in tweet.entities["polls"]:
                        if 'end_datetime' in polli:
                            poll = poll+","+polli["end_datetime"]

        tweetsHashtagsNumber.append(htNumber)
        tweetsHashtags.append(ht)
        tweetsMediaNumber.append(mediaNumber)
        tweetsMediaType.append(mediaType)
        tweetsMediaURLs.append(mediaURL)
        tweetsURLsNumber.append(URLNumber)
        tweetsURLs.append(urlstr)
        tweetsMentionsNumber.append(umNumber)
        tweetsMentions.append(um)
        tweetsSymbolsNumber.append(symNumber)
        tweetsSymbols.append(sym)
        tweetsPollsNumber.append(pollNumber)
        tweetsPolls.append(poll)

        '''if hasattr(tweet, 'favorited'):
            tweetsFavorited.append(tweet.favorited)
        else:
            tweetsFavorited.append("")

        if hasattr(tweet, 'retweeted'):
            tweetsRetweeted.append(tweet.retweeted)
        else:
            tweetsRetweeted.append("")'''

        if hasattr(tweet, 'possibly_sensitive'):
            tweetsPossibly_sensitive.append(tweet.possibly_sensitive)
        else:
            tweetsPossibly_sensitive.append("")

        if hasattr(tweet, 'filter_level'):
            tweetsFiltered_level.append(tweet.filter_level)
        else:
            tweetsFiltered_level.append("")

        if hasattr(tweet, 'lang'):
            tweetsLang.append(tweet.lang)
        else:
            tweetsLang.append("")

        matchingRulesNumber=0
        matchingRulesTag=""
        matchingRulesID=""
        if hasattr(tweet, 'matching_rules'):
            matchingRulesNumber = len(tweet.matching_rules)
            if tweet.matching_rules:
                for matchRi in tweet.matching_rules:
                    if 'tag' in matchRi:
                        matchingRulesTag = matchingRulesTag + "," + matchRi["tag"].encode("utf-8")
                    if 'id_str' in matchRi:
                        matchingRulesID = matchingRulesID + "," + matchRi["id_str"].encode("utf-8")

        tweetsMatching_rulesNumber.append(matchingRulesNumber)
        tweetsMatching_rulesTag.append(matchingRulesTag)
        tweetsMatching_rulesID.append(matchingRulesID)

    try:
        print uid
        print '' \
              ''
        post = {}
        #post['tweets'] = alltweets
        #post['tweets_details'] = outtweets
        post['user_id']=uid
        post['created_at'] = tweetsCreated_at
        post['id'] = tweetsID
        post['id_str'] = tweetsIDStr
        post['text'] = tweetsText
        post['source'] = tweetsSource
        post['truncated'] = tweetsTruncated
        post['in_reply_to_status_id_str'] = tweetsIn_reply_to_status_id_str
        post['in_reply_to_user_id_str'] = tweetsIn_reply_to_user_id_str
        post['in_reply_to_screen_name'] = tweetsIn_reply_to_screen_name
        post['coordinatesNumber'] = tweetsCoordinatesNumber
        post['coordinates'] = tweetsCoordinates
        post['coordinatesType'] = tweetsCoordinatesType

        post['placeCountry'] = tweetsPlaceCountry
        post['placeCountryCode'] = tweetsPlaceCountryCode
        post['placeFullName'] = tweetsPlaceFullName
        post['placeID'] = tweetsPlaceID
        post['placeName'] = tweetsPlaceName
        post['placeType'] = tweetsPlaceType
        post['placeURL'] = tweetsPlaceURL

        post['quoted_status_id_str'] = tweetsQuote_status
        post['is_quote_status'] = tweetsIs_quote_status
        post['retweeted_status'] = tweetsRetweet_status
        post['quote_count'] = tweetsQuote_count
        post['reply_count'] = tweetsReply_count
        post['retweet_count'] = tweetsRetweet_count
        post['favorite_count'] = tweetsFavorite_count

        post['hashtagsNumber'] = tweetsHashtagsNumber
        post['hashtags'] = tweetsHashtags
        post['urls'] = tweetsURLs
        post['urlsNumber'] = tweetsURLsNumber
        post['user_mentionsNumber'] = tweetsMentionsNumber
        post['user_mentions'] = tweetsMentions
        post['mediaNumber'] = tweetsMediaNumber
        post['mediaURLs'] = tweetsMediaURLs
        post['mediaType'] = tweetsMediaType
        post['symbolsNumber'] = tweetsSymbolsNumber
        post['symbols'] = tweetsSymbols
        post['pollsNumber'] = tweetsPollsNumber
        post['polls'] = tweetsPolls

        #post['favorited'] = tweetsFavorited
        #post['retweeted'] = tweetsRetweeted

        post['possibly_sensitive'] = tweetsPossibly_sensitive
        post['filter_level'] = tweetsFiltered_level
        post['lang'] = tweetsLang
        post['matching_rulesNumber'] = tweetsMatching_rulesNumber
        post['matching_rulesTag'] = tweetsMatching_rulesTag
        post['matching_rulesID'] = tweetsMatching_rulesID

        print ''
        print len(tweetsID)
        print ''
        return  post
    except Exception as e:
        print 'error in getting tweets for user: '+str(uid)
        print(e)


def checkifUserExist(uid):
    db_file = "/home/ubuntu/GTapp-virtualenv/helloworld/db.sqlite3"
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    cur = conn.cursor()
    cur.execute("SELECT * FROM GTapp_twitteruser WHERE id_str=?", (uid,))

    rows =  cur.fetchall()


    print ''
    print 'number of rows'
    print rows
    print ''
    if len(rows)>0:
        return True
    else:
        return False

def checkifTweetsExist(uid):
    db_file = "/home/ubuntu/GTapp-virtualenv/helloworld/db.sqlite3"
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    cur = conn.cursor()
    cur.execute("SELECT * FROM GTapp_tweets WHERE user_id=?", (uid,))

    rows =  cur.fetchall()

    print ''
    print 'number of rows'
    print rows
    print ''
    if len(rows)>0:
        return True
    else:
        return False

def checkifRatingsExist(uid):
    db_file = "/home/ubuntu/GTapp-virtualenv/helloworld/db.sqlite3"
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    cur = conn.cursor()
    cur.execute("SELECT * FROM GTapp_ratings WHERE user_id=?", (uid,))

    rows =  cur.fetchall()


    print ''
    print 'number of rows'
    print rows
    print ''
    if len(rows)>0:
        return True
    else:
        return False

def twitter_authenticated(request):
    print request.session['request_token_oauth_token']
    # Step 1. Use the request token in the session to build a new client.
    token = oauth.Token(request.session['request_token_oauth_token'],
                        request.session['request_token_oauth_token_secret'])
    token.set_verifier(request.GET['oauth_verifier'])
    client = oauth.Client(consumer, token)

    # Step 2. Request the authorized access token from Twitter.
    resp, content = client.request(access_token_url, "GET")
    if resp['status'] != '200':
        print content
        raise Exception("Invalid response from Twitter.")

    """
    This is what you'll get back from Twitter. Note that it includes the
    user's user_id and screen_name.
    {
        'oauth_token_secret': 'IcJXPiJh8be3BjDWW50uCY31chyhsMHEhqJVsphC3M',
        'user_id': '120889797',
        'oauth_token': '120889797-H5zNnM3qE0iFoTTpNEHIz3noL9FKzXiOxwtnyVOD',
        'screen_name': 'heyismysiteup'
    }
    """
    access_token = dict(cgi.parse_qsl(content))

    us=access_token['screen_name']
    # Step 3. Lookup the user or create them if they don't exist.
    try:
        user = User.objects.get(username=access_token['screen_name'])
    except User.DoesNotExist:
        # When creating the user I just use their screen_name@twitter.com
        # for their email and the oauth_token_secret for their password.
        # These two things will likely never be used. Alternatively, you
        # can prompt them for their email here. Either way, the password
        # should never be used.
        user = User.objects.create_user(access_token['screen_name'],
                                        '%s@twitter.com' % access_token['screen_name'],
                                        access_token['oauth_token_secret'])

        # Save our permanent token and secret for later.
        '''
        profile = Profile()
        profile.user = user
        profile.oauth_token = access_token['oauth_token']
        profile.oauth_secret = access_token['oauth_token_secret']
        profile.save()
        '''
    # Authenticate the user and log them in using Django's pre-built
    # functions for these things.
    user = authenticate(username=access_token['screen_name'],
                        password=access_token['oauth_token_secret'])

    print ''
    #print user['statuses.count']
    print ''
    #login(request, user)


    #home_timeline = oauth_req('https://api.twitter.com/1.1/statuses/home_timeline.json', settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
    user = oauth_req('https://api.twitter.com/1.1/users/show.json?screen_name='+us, settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
    #tweets = oauth_req('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='+us, settings.TWITTER_TOKEN,settings.TWITTER_SECRET)
    print ''
    print user
    print ''
    obj = json.loads(user)
    #u=ast.literal_eval(user)
    #get_all_tweets(obj["id"])
    if obj["statuses_count"] < 100:
        return render(request, 'userRatings/user/illegable.html', {'msg': 'Thank you for your interest '+obj["screen_name"]+', unfortunately in order to participate in this questionnaire you need to have an active twitter account with at least 100 tweets. You only have '+ str(obj["statuses_count"])+' tweets!'})
    elif checkifRatingsExist(obj["id_str"]):
        return render(request, 'userRatings/user/illegable.html', {'msg': 'Thank you for your interest ' + obj[
            "screen_name"] + ', you have already submitted your questionnaire, no need to resubmit'})
    else:
        request.session['usr'] = user
        # save user
        if checkifUserExist(obj["id_str"])==False:
            insert_user(obj)
        redirect_url='display_petitions'
        return redirect(redirect_url)
        #return render(request, 'userRatings/user/thankYou.html', {'msg': 'Thank you'})

        #return HttpResponseRedirect(redirect_url)
        #redirect_url = reverse(redirect_url, args=[l[1]])


def index(request):
    if request.method == 'POST':
        redirect_url='twitter_login'
        return redirect(redirect_url)
    else:
        return render(request, 'userRatings/user/info.html')




def display_petitions(request):
    # calls the PollForm we created and displays it on the page

    petitionsIDs = []
    petitionsTitles = []
    petitionsURLs = []
    displayPetitions=[]
    petitionsValues = []
    if 'usr' in request.session:
        usr = request.session['usr']
        usrObj = json.loads(usr)
        if checkifRatingsExist(usrObj["id_str"]):
            return render(request, 'userRatings/user/illegable.html', {'msg': 'Thank you for your interest ' + usrObj[
                "screen_name"] + ', you have already submitted your questionnaire, no need to resubmit'})
        msg="Hi "+usrObj["screen_name"]+", the online petitioning community is looking for your help to build a better recommendation system"
    else:
        msg=''
        print 'user is not retrieved at display_petitions'
    incomplete = False

    if request.method == 'POST':
        total=len(petitionsIDs)
        count=0
        if 'displayPetitions' in request.session:
            displayPetitions = request.session['displayPetitions']
        if 'petitionsIDs' in request.session:
            petitionsIDs = request.session['petitionsIDs']
        if 'petitionsURLs' in request.session:
            petitionsURLs = request.session['petitionsURLs']
        if 'petitionsTitles' in request.session:
            petitionsTitles = request.session['petitionsTitles']
            for id in petitionsIDs:
                val = request.POST.get(id, "-1")
                petitionsValues.append(val)
            for v in petitionsValues:
                if v=="-1":
                    incomplete = True
                    break
            if incomplete:
                msg = 'Please finish rating all the petitions according to your preference'
                displayPetitions = zip(petitionsIDs, petitionsURLs, petitionsTitles,petitionsValues)
                request.session['displayPetitions'] = displayPetitions
            else:
                request.session['petitionsValues'] = petitionsValues
                # save ratings and commit database for user, tweets, and ratings info
                insert_ratings(usrObj["id_str"],petitionsIDs,petitionsValues)

                # Route to another page for thank you
                msg = 'Thank you, '+usrObj["screen_name"]+", for helping the online petitioning community to build a better recommendation system!"
                return render_to_response('userRatings/user/thankYou.html',
                                          {'msg': msg},
                                          context_instance=RequestContext(request), )
        return render_to_response('userRatings/petition/rate.html', {'petitions': displayPetitions, 'msg': msg, 'incomplete': incomplete, 'val':petitionsValues},
                                          context_instance=RequestContext(request), )

    else:
        petitions = getRandomPetitions(10)

        for i in range(len(petitions[0])):
            petitionsIDs.append(str(petitions[0][i]))
            petitionsURLs.append(petitions[1][i])
            petitionsTitles.append(petitions[2][i])
        request.session['petitionsIDs'] = petitionsIDs
        request.session['petitionsURLs'] = petitionsURLs
        request.session['petitionsTitles'] = petitionsTitles
        displayPetitions = zip(petitionsIDs,petitionsURLs,petitionsTitles)
        request.session['displayPetitions'] = displayPetitions
        #return render(request, 'userRatings/petition/rate.html', {'petitions': petitions})

        #tweets = oauth_req('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=' + usrObj["screen_name"],
                           #settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
        if checkifTweetsExist(usrObj["id_str"]):
            tweets=get_all_tweets(int(usrObj["id_str"]))
            # Save users tweets
            insert_tweets(tweets)
        return render_to_response('userRatings/petition/rate.html', {'petitions': displayPetitions, 'msg': msg,'incomplete': incomplete, 'val':''}, context_instance=RequestContext(request), )
