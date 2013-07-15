from django.conf.urls import patterns, url
 
urlpatterns = patterns('gpao.views',
        url(r'^$', 'main_gpao', name='main_gpao'),
        url(r'^nm/$', 'liste_nm', name='liste_nm'),
        url(r'^nm/(?P<no_nm>NM-\d{4}-\d{2})/$', 'details_nm', name='details_nm'),
        url(r'^pe/$', 'liste_pe', name='liste_pe'),
    )