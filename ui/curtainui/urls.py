from django.conf.urls import patterns, url
from curtainui import views
#import sys
#print sys.path
urlpatterns = patterns('',
    url(r'^$', views.index , name='index'),
    url(r'^open$', views.Open , name='open'),
    url(r'^close$', views.Close , name='close'),
)
