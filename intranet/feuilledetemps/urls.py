from django.conf.urls import patterns, url
 
urlpatterns = patterns('feuilledetemps.views',

    url(r'^eci/blocs/$', 'add_blocs'),
    url(r'^eci/blocs/success/$', 'add_blocs_success'),
    
    url(r'^eci/banque/$', 'add_blocs_banque'),
    url(r'^eci/banque/success/$', 'add_blocs_banque_success'),
    
    url(r'^eci/rapports/$', 'index'),
    
    url(r'^eci/rapports/clients/$', 'liste_clients'),
    url(r'^eci/rapports/clients/getcsv/$', 'liste_clients_csv'),

    url(r'^eci/rapports/clients/(?P<client_id>\d+)/$', 'client_details'),

    url(r'^eci/rapports/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'listeblocs'),
    url(r'^eci/rapports/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/getcsv/$', 'listeblocs_csv'),
    
    url(r'^eci/rapports/projets/$', 'listerapports'),
    url(r'^eci/rapports/projets/getcsv/$', 'listerapports_csv'),
    
    url(r'^eci/rapports/projets-noms/(?P<nom_projet>\w+)/$', 'liste_nom_projet'),
    
    url(r'^eci/rapports/projets-noms/(?P<nom_projet>\w+)/(?P<modele_projet>[-A-Za-z0-9_]+)/$', 'liste_modele_projet'),
    
    url(r'^eci/rapports/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/$', 'rapportdetail'),
    url(r'^eci/rapports/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/getcsv/$', 'rapportdetail_csv'),

    url(r'^eci/rapports/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<numero_tache>[a-zA-Z]\d{2})/$', 'projettachedetail'),
    url(r'^eci/rapports/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<numero_tache>[a-zA-Z]\d{2})/getcsv/$', 'projettachedetailcsv'),
    
    url(r'^eci/rapports/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'projettemps'),
    url(r'^eci/rapports/projets/(?P<numero_projet>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/getcsv/$', 'projettemps_csv'),
    
    url(r'^eci/rapports/taches/$', 'listetaches'),
    url(r'^eci/rapports/taches/getcsv/$', 'listetaches_csv'),
    
    url(r'^eci/rapports/taches/(?P<numero_tache>[a-zA-Z]\d{2})/$', 'tachedetail'),
    url(r'^eci/rapports/taches/(?P<numero_tache>[a-zA-Z]\d{2})/getcsv/$', 'tachedetail_csv'),
    
    url(r'^eci/rapports/taches/(?P<numero_tache>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'tachetemps'),
    url(r'^eci/rapports/taches/(?P<numero_tache>[-A-Za-z0-9_]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/getcsv/$', 'tachetemps_csv'),
    
    url(r'^eci/rapports/employes/$', 'listeemployes'),
    url(r'^eci/rapports/employes/getcsv/$', 'liste_employes_csv'),
    
    url(r'^eci/rapports/employes/(?P<username>[A-Za-z]+)/$', 'employedetail'),
    url(r'^eci/rapports/employes/(?P<username>[A-Za-z]+)/getcsv/$', 'employedetail_csv'),
    
    url(r'^eci/rapports/employes/(?P<username>[A-Za-z]+)/details/$', 'employe_sommaire'),
    url(r'^eci/rapports/employes/(?P<username>[A-Za-z]+)/details/getcsv/$', 'employe_sommaire_csv'),
    
    url(r'^eci/rapports/employes/(?P<username>[A-Za-z]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$', 'employedetailperiode'),
    url(r'^eci/rapports/employes/(?P<username>[A-Za-z]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/getcsv/$', 'employe_detail_periode_csv'),
    
    )