"""
WSGI config for coveragePythonTest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import coverage,atexit
cov = coverage.Coverage(branch=True,config_file='.coveragerc')
cov.start()

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coveragePythonTest.settings")

application = get_wsgi_application()

def save_coverage():
    cov.stop()
    cov.save()

atexit.register(save_coverage)
