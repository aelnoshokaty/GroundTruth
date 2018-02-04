from django.contrib import admin

from .models import Petition, Tweets,TwitterUser,Ratings


#class UserAdmin(admin.ModelAdmin):
    #list_display = ['username','password']

#class ProfileAdmin(admin.ModelAdmin):
#    list_display = ['oauth_token','oauth_secret']


admin.site.register(Petition)
admin.site.register(Tweets)
admin.site.register(TwitterUser)
admin.site.register(Ratings)