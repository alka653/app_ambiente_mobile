"""
WSGI config for app_ambiente project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_ambiente.settings")

application = get_wsgi_application()

try:
	from dj_static import Cling

	application = Cling(get_wsgi_application())
except:
	pass