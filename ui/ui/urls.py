from django.conf.urls import include, url
from django.contrib import admin
import clock

urlpatterns = [
    # Examples:
    # url(r'^$', 'ui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('clock.urls')),
    url(r'^clock/', include('clock.urls')),
]
