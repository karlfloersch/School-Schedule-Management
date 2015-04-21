from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socs.settings')

app = Celery('socs', backend='amqp://guest:guest@localhost//', broker='amqp://', include=['schedules.tasks'])
app.conf.update(CELERY_RESULT_BACKEND='amqp')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
#app.config_from_object('django.conf:settings')
app.conf.update(
	BROKER_URL = 'amqp://guest:guest@localhost//',
	CELERY_ACCEPT_CONTENT = ['json', 'pickle'],
	CELERY_EVENT_SERIALIZER = 'json',
	CELERY_TASK_SERIALIZER = 'json',
	CELERY_RESULT_SERIALIZER = 'json',
# CELERY_RESULT_BACKEND = 'amqp'
	CELERY_TIMEZONE = 'US/Mountain',
	CELERY_RESULT_PERSISTENT = True,
	CELERY_TASK_RESULT_EXPIRES = 1000, # seconds
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
	CELERY_DEFAULT_QUEUE = 'tasks',
# CELERY_TRACK_STARTED = True
# CELERY_LOG_DIR="/var/log/celery"
# CELERY_LOG_FILE="celery.log"
	CELERY_IMPORTS=("schedules.tasks")
	)

from kombu import Queue
CELERY_QUEUES = (Queue('tasks', routing_key='task.#'),
                 Queue('frontend_tasks', routing_key='frontend.#'),
                )

CELERY_DEFAULT_ROUTING_KEY = 'task.default'
CELERY_DEFAULT_EXCHANGE = 'tasks'

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
