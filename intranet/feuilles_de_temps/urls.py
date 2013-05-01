from django.conf.urls import patterns, url
 
urlpatterns = patterns('feuilles_de_temps.views',

    url(r'^blocs/eci/$', 'add_blocs_eci', name='add_blocs_eci'),
    url(r'^blocs/eci/success/$', 'success', name='success'),
    url(r'^banque/$', 'add_banque', name='add_banque'),
    url(r'^banque/success/$', 'success', name='success'),
    )