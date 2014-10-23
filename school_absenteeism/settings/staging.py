from school_absenteeism.settings.base import *

os.environ.setdefault('CACHE_HOST', '127.0.0.1:11211')
os.environ.setdefault('BROKER_HOST', '127.0.0.1:5672')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES['default']['NAME'] = 'school_absenteeism_staging'
DATABASES['default']['USER'] = 'school_absenteeism_staging'
DATABASES['default']['HOST'] = os.environ.get('DB_HOST', '')
DATABASES['default']['PORT'] = os.environ.get('DB_PORT', '')
DATABASES['default']['PASSWORD'] = os.environ['DB_PASSWORD']

WEBSERVER_ROOT = '/var/www/school_absenteeism/'

PUBLIC_ROOT = os.path.join(WEBSERVER_ROOT, 'public')

STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')

MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

LOGGING['handlers']['file']['filename'] = os.path.join(WEBSERVER_ROOT, 'log', 'school_absenteeism.log')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '%(CACHE_HOST)s' % os.environ,
    }
}

EMAIL_SUBJECT_PREFIX = '[School_Absenteeism Staging] '

COMPRESS_ENABLED = True

SESSION_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(';')

# Uncomment if using celery worker configuration
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'amqp://school_absenteeism_staging:%(BROKER_PASSWORD)s@%(BROKER_HOST)s/school_absenteeism_staging' % os.environ
