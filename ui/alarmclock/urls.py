from django.conf.urls import patterns, url
from alarmclock import views

urlpatterns = patterns('',
    url(r'^$', views.index , name='index'),
    url(r'^setalarmtime$', views.setalarmtime , name='setalarmtime'),
    url(r'^status$', views.status , name='status'),
)
