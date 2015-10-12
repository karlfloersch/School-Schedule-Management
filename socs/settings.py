"""
Django settings for socs project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep thefewjiofewoj secret key used in production secret!
SECRET_KEY = '9+m2ev46dfdsajofweiofwes6d#2-c&c1g8fol308%czdu0@b_f(qw-5#r54m&%6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'schedules',
    'djcelery',
    'sslserver',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'socs.urls'

WSGI_APPLICATION = 'socs.wsgi.application'

#################################################
BROKER_URL = 'amqp://guest:guest@localhost//'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_EVENT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
#CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'amqp'
CELERY_TIMEZONE = 'US/Mountain'
CELERY_RESULT_PERSISTENT = True
CELERY_TASK_RESULT_EXPIRES = 1000 # seconds
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_DEFAULT_QUEUE = 'tasks'
CELERY_TRACK_STARTED = True
CELERY_LOG_DIR="/var/log/celery"
CELERY_LOG_FILE="celery.log"
CELERY_IMPORTS=("schedules.tasks")

from kombu import Queue

CELERY_QUEUES = (Queue('tasks', routing_key='task.#'),
                 Queue('frontend_tasks', routing_key='frontend.#'),
                )

CELERY_DEFAULT_ROUTING_KEY = 'task.default'
CELERY_DEFAULT_EXCHANGE = 'tasks'
#############################################################


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'schedules/templates',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

LOGIN_URL = '/login/'

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

# Allow for log file creation 
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': SITE_ROOT + "/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'schedules': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s %(levelname)s [%(name)s: %(lineno)s] -- %(message)s',
#             'datefmt': '%m-%d-%Y %H:%M:%S'
#         },
#     },
#     'handlers': {
#         'logfile': {
#             'level': 'INFO',
#             'filters': None,
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': '/logs/celery/celer.log',
#             'maxBytes': 1024*1024*5,
#             'backupCount': 3,
#             'formatter': 'standard'
#         },
#         'debug_logfile': {
#             'level': 'DEBUG',
#             'filters': None,
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': '/logs/celery/celer.log',
#             'maxBytes': 1024*1024*5,
#             'backupCount': 5,
#             'formatter': 'standard'
#         },
#         'default_logger': {
#             'level': 'WARNING',
#             'filters': None,
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': '/logs/celery/celer.log',
#             'maxBytes': 1024*1024*5,
#             'backupCount': 2,
#             'formatter': 'standard'
#         },
#         'celery_logger': {
#             'level': 'DEBUG',
#             'filters': None,
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': '/logs/celery/celer.log',
#             'maxBytes': 1024*1024*5,
#             'backupCount': 2,
#             'formatter': 'standard'
#         },
#         'celery_task_logger': {
#             'level': 'DEBUG',
#             'filters': None,
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': '/logs/celery/celer.log',
#             'maxBytes': 1024*1024*5,
#             'backupCount': 2,
#             'formatter': 'standard'
#         },
#     },
#     'loggers': {
#         '': {
#             'handlers': ['default_logger'],
#             'level': 'WARNING',
#             'propagate': True,
#         },
#         'django': {
#             'handlers': ['logfile'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'feedmanager': {
#             'handlers': ['logfile', 'debug_logfile'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'recipemanager': {
#             'handlers': ['logfile', 'debug_logfile'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'menumanager': {
#             'handlers': ['logfile', 'debug_logfile'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'celery.task': {
#             'handlers': ['celery_task_logger'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'celery': {
#             'handlers': ['celery_logger'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     }
# }
