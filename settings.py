# Django settings for project.
# you can override any of this with settings_user.py, which does not get
# committed to source control.

import os
import datetime

def absolute(relative_path):
    "make a relative path absolute"
    return os.path.normpath(os.path.join(os.path.dirname(__file__), relative_path))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Andy Kelley', 'superjoe30@gmail.com'),
)

MANAGERS = ADMINS

# this is something you may want to override in settings_user.py
DATABASES = {
    'default': {
        'NAME': 'solidcomposer',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'dev',
        'PASSWORD': 'dev',
    },
}

# South
SOUTH_LOGGING_ON = False
SOUTH_LOGGING_FILE = absolute("south.log")
SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.

# set this to None as soon as django supports it.
# this is something you may want to override in settings_user.py
TIME_ZONE = 'America/Phoenix'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = absolute('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
# this is something you may want to override in settings_user.py
MEDIA_URL = 'http://localhost:8080/django/solidcomposer/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
# this is something you may want to override in settings_user.py
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2_l-92-j(^)a=vsynmsw1d(efi!w@w#j#v@ucv^2i7cfsk=!8='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    absolute('templates'),
)

# where processed java script files will be output to. folder structure
# will be mirrored.
PREPARSE_OUTPUT = os.path.join(MEDIA_ROOT, 'js', 'pre')

# these will be processed with django's templating system and moved
# to the PREPARSE_OUTPUT folder, mirroring folder structure.
PREPARSE_DIR = os.path.join('templates', 'preparsed')

# the dictionary that will be available to your preparsed code.
PREPARSE_CONTEXT = {
    'server_time': datetime.datetime.today().strftime("%B %d, %Y %H:%M:%S"),
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'context.global_values',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'south',
    'django_extensions',
    'main',
    'competitions',
    'chat',
    'workshop',
    'music',
)

LOGIN_URL = "/login/"
AUTH_PROFILE_MODULE = 'main.Profile'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# how many seconds to wait before generating leave messages for chatters
CHAT_TIMEOUT = 60

# maximum length of competition tracks in seconds
COMPO_ENTRY_MAX_LEN = 10 * 60

# minimum amount of time to give users for a competition in minutes
MINIMUM_COMPO_LENGTH = 10

# how many seconds to wait between tracks in listening party for buffering
LISTENING_PARTY_BUFFER_TIME = 10

# how many bytes to limit uploads to
FILE_UPLOAD_SIZE_CAP = 1024 * 1024 * 20  # 20 MB

# for pagination
ITEMS_PER_PAGE = 5

# how long does a user have to activate before it expires
ACTIVATION_EXPIRE_DAYS = 1

# free acount info
# how much disk space do bands get for freeeee
BAND_INIT_SPACE = 1024 * 1024 * 1024 * 0.5 # 0.5 GB
# how many bands can free users create
FREE_BAND_LIMIT = 10

# amazon s3 details
AWS_ACCESS_KEY_ID = 'AKIAII3Z2JMVTAJ6R4CQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'solidcomposer'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# leave this at the very end
if os.path.exists("settings_user.py"):
    from settings_user import *
