"""
Django settings for pramari project.
"""

from .defaults import *

print("Development Settings!")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Allow all host headers
ALLOWED_HOSTS = ['*']

DOCS_ROOT = BASE_DIR + '/docs/output/html/'
COVERAGE_ROOT = BASE_DIR + '/htmlcov/'

DATABASES = {}
DATABASES['default'] = {}
DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = 'django.db'

# CACHES
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
