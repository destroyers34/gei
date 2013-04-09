from django.conf.urls import patterns, url
 
urlpatterns = patterns('fournisseurs.views',
	url(r'^(?P<fournisseur_id>\d+)/$', 'detail_fournisseur'),
)