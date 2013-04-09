from django.conf.urls import patterns, url
 
urlpatterns = patterns('machines.views',

    url(r'^fournisseurs/$', 'liste_fournisseurs'),
    url(r'^(?P<fournisseur_id>\d+)/$', 'liste_machines'),
    url(r'^(?P<fournisseur_id>\d+)/(?P<machine_id>\d+)$', 'detail_machine'),
    )