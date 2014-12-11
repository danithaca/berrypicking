"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

# daniel's notes:
# 1. to reload updated content, do "touch wsgi.py" to trigger reload.
# 2. to serve static files, need to
# a) set STATIC_ROOT in settings.py,
# b) use manage.py collectstatic,
# c) set apache conf to bypass /static

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
