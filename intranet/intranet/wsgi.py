import os
import sys

sys.path.append('C:/intranetdjango')
sys.path.append('C:/intranetdjango/intranet')

os.environ['DJANGO_SETTINGS_MODULE'] = 'intranet.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()