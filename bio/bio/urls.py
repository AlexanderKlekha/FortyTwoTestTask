from django.conf.urls import patterns, include, url

from django.contrib import admin
from person.views import PersonIndexView
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', PersonIndexView.as_view(), name='index'),
                       )
