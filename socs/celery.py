from __future__ import absolute_import

import os

from celery import Celery
from kombu import Exchange
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
	CELERY_ACCEPT_CONTENT = ['json'],
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
# CELERY_QUEUES = (Queue('tasks', routing_key='task.#'),
#                  Queue('frontend_tasks', routing_key='frontend.#'),
#                 )

CELERY_QUEUES = (
	Queue('tasks', Exchange('tasks'), routing_key='task.#'),
	Queue('write_tasks', Exchange('write_tasks'), routing_key='write_tasks'),
	Queue('read_tasks', Exchange('read_tasks'), routing_key='read_tasks'),
)

CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'task.default'
CELERY_DEFAULT_EXCHANGE = 'tasks'

CELERY_ROUTES = {
	'schedules.tasks.add_students_to_database_two': {'queue': 'write_tasks'},
	'schedules.tasks.remove_school': {'queue': 'write_tasks'},
	'schedules.tasks.get_normal_schedule_two': {'queue': 'read_tasks'},
	'schedules.tasks.add_classes_to_database_two': {'queue': 'write_tasks'},
	'schedules.tasks.send_a_friend_request_two': {'queue': 'write_tasks'},
	'schedules.tasks.delete_friend_from_friends_list_two': {'queue': 'write_tasks'},
	'schedules.tasks.get_schools_address_two': {'queue': 'read_tasks'},
	'schedules.tasks.delete_school_from_database_two': {'queue': 'write_tasks'},
	'schedules.tasks.search_all_students_two': {'queue': 'read_tasks'},
	'schedules.tasks.search_school_from_database_two': {'queue': 'read_tasks'},
	'schedules.tasks.edit_school_to_database_two': {'queue': 'write_tasks'},
	'schedules.tasks.add_school_to_database_two': {'queu:e': 'write_tasks'},
	'schedules.tasks.accept_friend_request_two': {'queue': 'write_tasks'},
	'schedules.tasks.deny_friend_request_two': {'queue': 'write_tasks'},
	'schedules.tasks.get_friend_request_two': {'queue': 'read_tasks'},
	'schedules.tasks.possible_friends': {'queue': 'read_tasks'},
	'schedules.tasks.get_a_person': {'queue': 'read_tasks'},
	'schedules.tasks.get_friends_list_two': {'queue': 'read_tasks'},
	'schedules.tasks.find_school_two': {'queue': 'read_tasks'},
	'schedules.tasks.get_overlapping_friends_by_specific_course_two': {'queue': 'read_tasks'},
	}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
