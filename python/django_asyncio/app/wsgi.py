"""
WSGI config for bl project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from aiohttp import web
from aiohttp_wsgi import WSGIHandler

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
wsgi_handler = WSGIHandler(application)
app = web.Application()
