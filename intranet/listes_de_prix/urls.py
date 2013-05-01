from django.conf.urls import patterns, url
 
urlpatterns = patterns('listes_de_prix.views',

    url(r'^fournisseurs/$', 'liste_fournisseurs', name='liste_fournisseurs'),
    url(r'^fournisseurs/(?P<fournisseur_id>\d+)/$', 'detail_fournisseur', name='detail_fournisseur'),
    url(r'^(?P<fournisseur_id>\d+)/$', 'liste_machines', name='liste_machines'),
    url(r'^(?P<fournisseur_id>\d+)/(?P<machine_id>\d+)$', 'details_machine', name='details_machine'),
    )