"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

#application = get_wsgi_application()

import os
import sys
#sys.path.append('/opt/bitnami/apps/django/django_projects/Django-mysite')
sys.path.insert(0, '/opt/bitnami/apps/django/django_projects/Django-mysite')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
