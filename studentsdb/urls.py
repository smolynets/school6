from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'students.views.podii', name='podii'),
    url(r'^biblioteka/$', 'students.views.biblioteka', name='biblioteka'),
    url(r'^vuhovna/$', 'students.views.vyhovna', name='vyhovna'),
    url(r'^muzey/$', 'students.views.muzey', name='muzey'),
    url(r'^kolek/$', 'students.views.kolek', name='kolek'),
    url(r'^psuholoh/$', 'students.views.psuholoh', name='psuholoh'),
    url(r'^zno/$', 'students.views.zno', name='zno'),
    url(r'^rozlad/$', 'students.views.rozlad', name='rozlad'),
    url(r'^istoria/$', 'students.views.istoria', name='istoria'),


    url(r'^admin/', include(admin.site.urls)),
)
