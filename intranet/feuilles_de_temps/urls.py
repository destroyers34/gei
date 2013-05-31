from django.conf.urls import patterns, url
 
urlpatterns = patterns('feuilles_de_temps.views',

    url(r'^blocs/eci/$', 'blocs_eci', name='blocs_eci'),
    url(r'^blocs/eci/(?P<username>[A-Za-z]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'consultation_blocs_eci', name='consultation_blocs_eci'),
    url(r'^blocs/eci/add$', 'add_blocs_eci', name='add_blocs_eci'),
    url(r'^blocs/eci/success/$', 'success', name='success'),
    url(r'^blocs/tpe/$', 'add_blocs_tpe', name='add_blocs_tpe'),
    url(r'^blocs/tpe/success/$', 'success', name='success'),
    url(r'^banque/$', 'add_banque', name='add_banque'),
    url(r'^banque/success/$', 'success', name='success'),
    )