import os
import sys

sys.path.append('C:/ProjetGEI/IntranetGEI')
sys.path.append('C:/ProjetGEI/IntranetGEI/intranet')

os.environ['DJANGO_SETTINGS_MODULE'] = 'intranet.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()