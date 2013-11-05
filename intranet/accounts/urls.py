﻿from django.conf.urls import *

urlpatterns = patterns('',
                       (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),

                       (r'^logout/$', 'django.contrib.auth.views.logout',
                        {'template_name': 'accounts/logged_out.html'}),

                       (r'^password_change/$', 'django.contrib.auth.views.password_change',
                        {'template_name': 'accounts/password_change_form.html'}),

                       (r'^password_change/done/$', 'django.contrib.auth.views.password_change_done',
                        {'template_name': 'accounts/password_change_done.html'}),
                       )
