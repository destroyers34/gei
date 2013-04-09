from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^$', 'intranet.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fournisseurs/', include('fournisseurs.urls')),
    url(r'^feuilledetemps/', include('feuilledetemps.urls')),
    url(r'^liste-de-prix/', include('machines.urls')),
    #url(r'^report_builder/', include('report_builder.urls')),
    url(r'^accounts/', include('accounts.urls')),
)

urlpatterns += staticfiles_urlpatterns()