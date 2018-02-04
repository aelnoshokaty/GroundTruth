"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from GTapp import views
from django.conf.urls import *
from django.contrib import admin
from GTapp.views import twitter_login, twitter_logout, \
    twitter_authenticated

admin.autodiscover()
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^display_petitions/$', views.display_petitions, name='display_petitions'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/?$', views.twitter_login, name='twitter_login'),
    url(r'^logout/?$', views.twitter_logout),
    url(r'^login/authenticated/?$', views.twitter_authenticated,name='twitter_authenticated'),
#)


    #url(r'^user/(?P<id>\d+)/', views.user_detail, name='user_detail'),
    #url(r'^display_petitions/(?P<username>[\w\-]+)/$',views.display_petitions, name ='display_petitions'),
    #url(r'^$', views.home, name='home'),
    #url(r'^user/(?P<id>\d+)/', views.user_detail, name='user_detail'),


    #url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    #url(r'^oauth/', include('social_django.urls', namespace='social')),
    #url(r'^settings/$', views.settings, name='settings'),
    #url(r'^settings/password/$', views.password, name='password'),
    #url(r'^login/?$', views.twitter_login),
    #url(r'^logout/?$', views.twitter_logout),
    #url(r'^login/authenticated/?$', views.twitter_authenticated),
    url(r'^admin/', admin.site.urls),

]

