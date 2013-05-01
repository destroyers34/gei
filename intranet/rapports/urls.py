from django.conf.urls import patterns, url
 
urlpatterns = patterns('rapports.views',
    
    url(r'^eci/clients/$', 'liste_clients_eci', name='liste_clients_eci'),
    
    url(r'^eci/clients/xls/$', 'xls_liste_clients_eci', name='xls_liste_clients_eci'),
    
    url(r'^eci/clients/print/$', 'print_liste_clients_eci', name='print_liste_clients_eci'),
    
    #url(r'^eci/clients/getcsv/$', 'liste_clients_csv'),

    #url(r'^eci/clients/(?P<client_id>\d+)/$', 'client_details'),
    #url(r'^eci/clients/(?P<client_id>\d+)/getcsv/$', 'client_details_csv'),

    #url(r'^eci/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'listeblocs'),
    #url(r'^eci/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/getcsv/$', 'listeblocs_csv'),
    
    #url(r'^eci/complet/(?P<numero_projet>[-A-Za-z0-9_]+)/$', 'rapport_complet'),
    
    #url(r'^eci/projets/$', 'listerapports'),
    #url(r'^eci/projets/getcsv/$', 'listerapports_csv'),
    
    #url(r'^eci/projets-noms/(?P<nom_projet>\w+)/$', 'liste_nom_projet'),
    #url(r'^eci/projets-noms/(?P<nom_projet>\w+)/getcsv/$', 'liste_nom_projet_csv'),
    
    #url(r'^eci/projets-noms/(?P<nom_projet>\w+)/(?P<modele_projet>[-A-Za-z0-9_]+)/$', 'liste_modele_projet'),
    #url(r'^eci/projets-noms/(?P<nom_projet>\w+)/(?P<modele_projet>[-A-Za-z0-9_]+)/getcsv/$', 'liste_modele_projet_csv'),
    
    #url(r'^eci/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/$', 'rapportdetail'),
    #url(r'^eci/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/getcsv/$', 'rapportdetail_csv'),

    #url(r'^eci/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<numero_tache>[a-zA-Z]\d{2})/$', 'projettachedetail'),
    #url(r'^eci/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<numero_tache>[a-zA-Z]\d{2})/getcsv/$', 'projettachedetailcsv'),
    
    #url(r'^eci/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'projettemps'),
    #url(r'^eci/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/getcsv/$', 'projettemps_csv'),
    
    #url(r'^eci/taches/$', 'listetaches'),
    #url(r'^eci/taches/getcsv/$', 'listetaches_csv'),
    
    #url(r'^eci/taches/(?P<numero_tache>[a-zA-Z]\d{2})/$', 'tachedetail'),
    #url(r'^eci/taches/(?P<numero_tache>[a-zA-Z]\d{2})/getcsv/$', 'tachedetail_csv'),
    
    #url(r'^eci/taches/(?P<numero_tache>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'tachetemps'),
    #url(r'^eci/taches/(?P<numero_tache>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/getcsv/$', 'tachetemps_csv'),
    
    #url(r'^eci/employes/$', 'listeemployes'),
    #url(r'^eci/employes/getcsv/$', 'liste_employes_csv'),
    
    #url(r'^eci/employes/(?P<username>[A-Za-z]+)/$', 'employedetail'),
    #url(r'^eci/employes/(?P<username>[A-Za-z]+)/getcsv/$', 'employedetail_csv'),
    
    #url(r'^eci/employes/(?P<username>[A-Za-z]+)/details/$', 'employe_sommaire'),
    #url(r'^eci/employes/(?P<username>[A-Za-z]+)/details/getcsv/$', 'employe_sommaire_csv'),
    
    #url(r'^eci/employes/(?P<username>[A-Za-z]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'employedetailperiode'),
    #url(r'^eci/employes/(?P<username>[A-Za-z]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/getcsv/$', 'employe_detail_periode_csv'),
    
    )