from django.conf.urls import include, url
from django.contrib import admin
import alarmclock, curtainui, mainpage

urlpatterns = [
    # Examples:
    # url(r'^$', 'ui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('mainpage.urls')),
    url(r'^alarmclock/', include('alarmclock.urls')),
    url(r'^curtain/', include('curtainui.urls')),
]
