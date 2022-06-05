"""
WSGI config for develop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
'''from whiteNoise import whiteNoise
from my_project import MyWSGIApp'''

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'develop.settings')

application = get_wsgi_application()
'''application=MyWSGIApp()
application=whiteNoise(application,root="/path/to/static/files")
application.add_files("/path/to/more/static/files",prefix="more-files/")'''
