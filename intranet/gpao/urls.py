from django.conf.urls import patterns, url
 
urlpatterns = patterns('gpao.views',
        url(r'^$', 'main_gpao', name='main_gpao'),
    )