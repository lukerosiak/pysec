
from settings import PROJECT_ROOT

DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# Python dotted path to the WSGI application used by Django's runserver; added in v1.4
WSGI_APPLICATION = 'wsgi.application'

############### PYSEC specific variables

# assumes this directory exists
DATA_DIR = "%s/pysec/data/" % PROJECT_ROOT