from django.conf.urls import patterns, url
from mainpage import views
import sys
print sys.path
urlpatterns = patterns('',
    url(r'^$', views.index , name='index'),
    url(r'^index$', views.index , name='index'),
)
