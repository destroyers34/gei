from django.conf.urls import patterns, url
 
urlpatterns = patterns('rapports.views',
    
    url(r'^eci/projets/$', 'liste_projets_eci', name='liste_projets_eci'),
    url(r'^eci/projets/numero/(?P<numero_projet>[-A-Za-z0-9_]+)/$', 'projet_details_eci', name='projet_details_eci'),
    url(r'^eci/projets/nom/(?P<nom_projet>\w+)/$', 'liste_projets_noms_eci', name='liste_projets_noms_eci'),
    url(r'^eci/projets/modele/(?P<nom_projet>\w+)/(?P<modele_projet>[-A-Za-z0-9_]+)/$', 'liste_projets_modeles_eci', name='liste_projets_modeles_eci'),
    url(r'^eci/projets/complet/(?P<numero_projet>[-A-Za-z0-9_]+)/$', 'rapport_complet_eci', name='rapport_complet_eci'),
    url(r'^eci/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<numero_tache>[a-zA-Z]\d{2})/$', 'projet_tache_details_eci', name='projet_tache_details_eci'),
    url(r'^eci/clients/$', 'liste_clients_eci', name='liste_clients_eci'),
    url(r'^eci/clients/(?P<client_id>\d+)/$', 'client_details_eci', name='client_details_eci'),
    url(r'^eci/taches/$', 'liste_taches_eci', name='liste_taches_eci'),
    url(r'^eci/taches/numero/(?P<numero_tache>[a-zA-Z]\d{2})/$', 'tache_details_eci', name='tache_details_eci'),
    url(r'^eci/employes/$', 'liste_employes_eci', name='liste_employes_eci'),
    url(r'^eci/employes/details/(?P<username>[A-Za-z]+)/$', 'employe_details_eci', name='employe_details_eci'),
    url(r'^eci/employes/(?P<username>[A-Za-z]+)/$', 'employe_blocs_eci', name='employe_blocs_eci'),
    url(r'^eci/employes/(?P<username>[A-Za-z]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'employe_blocs_periode_eci', name='employe_blocs_periode_eci'),
    url(r'^eci/projets/numero/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'projet_periode_eci', name='projet_periode_eci'),
    url(r'^eci/taches/numero/(?P<numero_tache>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'tache_periode_eci', name='tache_periode_eci'),

    url(r'^tpe/projets/$', 'liste_projets_tpe', name='liste_projets_tpe'),

    
    url(r'^eci/clients/xls/$', 'xls_liste_clients_eci', name='xls_liste_clients_eci'),
    url(r'^eci/clients/(?P<client_id>\d+)/xls/$', 'xls_client_details_eci', name='xls_client_details_eci'),    
    url(r'^eci/projets/xls/$', 'xls_liste_projets_eci', name='xls_liste_projets_eci'),
    url(r'^eci/taches/xls/$', 'xls_liste_taches_eci', name='xls_liste_taches_eci'),
    url(r'^eci/employes/xls/$', 'xls_liste_employes_eci', name='xls_liste_employes_eci'),
    url(r'^eci/projets/numero/(?P<numero_projet>[-A-Za-z0-9_]+)/xls/$', 'xls_projet_details_eci', name='xls_projet_details_eci'),
    url(r'^eci/taches/numero/(?P<numero_tache>[a-zA-Z]\d{2})/xls/$', 'xls_tache_details_eci', name='xls_tache_details_eci'),
    url(r'^eci/projets/nom/(?P<nom_projet>\w+)/xls/$', 'xls_liste_projets_noms_eci', name='xls_liste_projets_noms_eci'),
    url(r'^eci/projets/modele/(?P<nom_projet>\w+)/(?P<modele_projet>[-A-Za-z0-9_]+)/xls/$', 'xls_liste_projets_modeles_eci', name='xls_liste_projets_modeles_eci'),
    url(r'^eci/projets/complet/(?P<numero_projet>[-A-Za-z0-9_]+)/xls/$', 'xls_rapport_complet_eci', name='xls_rapport_complet_eci'),
    url(r'^eci/employes/details/(?P<username>[A-Za-z]+)/xls/$', 'xls_employe_details_eci', name='xls_employe_details_eci'),
    url(r'^eci/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<numero_tache>[a-zA-Z]\d{2})/xls/$', 'xls_projet_tache_details_eci', name='xls_projet_tache_details_eci'),
    url(r'^eci/employes/(?P<username>[A-Za-z]+)/xls/$', 'xls_employe_blocs_eci', name='xls_employe_blocs_eci'),
    url(r'^eci/employes/(?P<username>[A-Za-z]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/xls/$', 'xls_employe_blocs_periode_eci', name='xls_employe_blocs_periode_eci'),
    url(r'^eci/projets/numero/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/xls/$', 'xls_projet_periode_eci', name='xls_projet_periode_eci'),
    url(r'^eci/taches/numero/(?P<numero_tache>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/xls/$', 'xls_tache_periode_eci', name='xls_tache_periode_eci'),
    
    url(r'^tpe/projets/xls/$', 'xls_liste_projets_tpe', name='xls_liste_projets_tpe'),

    
    url(r'^eci/clients/print/$', 'print_liste_clients_eci', name='print_liste_clients_eci'),
    url(r'^eci/clients/(?P<client_id>\d+)/print/$', 'print_client_details_eci', name='print_client_details_eci'),  
    url(r'^eci/projets/attente/print/$', 'print_liste_projets_attente_eci', name='print_liste_projets_attente_eci'),
    url(r'^eci/projets/actif/print/$', 'print_liste_projets_actif_eci', name='print_liste_projets_actif_eci'),
    url(r'^eci/projets/completer/print/$', 'print_liste_projets_complet_eci', name='print_liste_projets_complet_eci'),
    url(r'^eci/taches/print/$', 'print_liste_taches_eci', name='print_liste_taches_eci'),
    url(r'^eci/employes/print/$', 'print_liste_employes_eci', name='print_liste_employes_eci'),
    url(r'^eci/projets/numero/(?P<numero_projet>[-A-Za-z0-9_]+)/print/$', 'print_projet_details_eci', name='print_projet_details_eci'),
    url(r'^eci/taches/numero/(?P<numero_tache>[a-zA-Z]\d{2})/print/$', 'print_tache_details_eci', name='print_tache_details_eci'),
    url(r'^eci/projets/nom/(?P<nom_projet>\w+)/print/$', 'print_liste_projets_noms_eci', name='print_liste_projets_noms_eci'),
    url(r'^eci/projets/modele/(?P<nom_projet>\w+)/(?P<modele_projet>[-A-Za-z0-9_]+)/print/$', 'print_liste_projets_modeles_eci', name='print_liste_projets_modeles_eci'),
    url(r'^eci/projets/complet/(?P<numero_projet>[-A-Za-z0-9_]+)/print/$', 'print_rapport_complet_eci', name='print_rapport_complet_eci'),
    url(r'^eci/employes/details/(?P<username>[A-Za-z]+)/print/$', 'print_employe_details_eci', name='print_employe_details_eci'),
    url(r'^eci/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<numero_tache>[a-zA-Z]\d{2})/print/$', 'print_projet_tache_details_eci', name='print_projet_tache_details_eci'),
    url(r'^eci/employes/(?P<username>[A-Za-z]+)/print/$', 'print_employe_blocs_eci', name='print_employe_blocs_eci'),
    url(r'^eci/employes/(?P<username>[A-Za-z]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/print/$', 'print_employe_blocs_periode_eci', name='print_employe_blocs_periode_eci'),
    url(r'^eci/projets/numero/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/print/$', 'print_projet_periode_eci', name='print_projet_periode_eci'),
    url(r'^eci/taches/numero/(?P<numero_tache>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/print/$', 'print_tache_periode_eci', name='print_tache_periode_eci'),

    url(r'^tpe/projets/attente/print/$', 'print_liste_projets_attente_tpe', name='print_liste_projets_attente_tpe'),
    url(r'^tpe/projets/actif/print/$', 'print_liste_projets_actif_tpe', name='print_liste_projets_actif_tpe'),
    url(r'^tpe/projets/completer/print/$', 'print_liste_projets_complet_tpe', name='print_liste_projets_complet_tpe'),
    )