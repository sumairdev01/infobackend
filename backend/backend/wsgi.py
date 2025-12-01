"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Add the project directory to the sys.path
# This ensures that 'backend.settings' can be imported correctly
# regardless of the current working directory
path = Path(__file__).resolve().parent.parent
if str(path) not in sys.path:
    sys.path.append(str(path))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()

app = application
