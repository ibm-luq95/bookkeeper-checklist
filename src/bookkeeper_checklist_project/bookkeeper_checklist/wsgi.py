"""
WSGI config for bookkeeper_checklist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

# dotenv_path = os.path.join("/home/ibrahim/bookkeeper-checklist/src", ".env")
# load_dotenv(dotenv_path=dotenv_path)  # load all environment variables from .env.
load_dotenv()

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookkeeper_checklist.settings")

application = get_wsgi_application()
