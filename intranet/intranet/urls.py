from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'intranet.views.index'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^listesdeprix/', include('listes_de_prix.urls')),
    url(r'^feuillesdetemps/', include('feuilles_de_temps.urls')),
    url(r'^rapports/', include('rapports.urls')),
    url(r'^gpao/', include('gpao.urls')),
)

urlpatterns += staticfiles_urlpatterns()