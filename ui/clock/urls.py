from django.conf.urls import patterns, url
from clock import views

urlpatterns = patterns('',
    url(r'^$', views.index , name='index'),
    url(r'^setalarmtime$', views.setalarmtime , name='setalarmtime'),
)
