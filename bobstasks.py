from __future__ import absolute_import
from celery import shared_task
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
import pymongo
import json
from celery import Task
from pymongo import MongoClient
from bson.dbref import DBRef
client = MongoClient()

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


class CallbackTask(Task):
		def on_success(self, retval, task_id, args, kwargs):
			pass

		def on_failure(self, exc, task_id, args, kwargs, einfo):
			pass

@shared_task
def add_students_to_database():
	db = client.students
	dat_base_var = "students"
	first_name_var = "jimmy"
	last_name_var = "jam"
	email_stuff = "jimmy@gmail.com"
	school_name= "magic school bus"
	info ={"first_name" : first_name_var,"last_name" : last_name_var, "list":[]}
	original_id =db.friends_list.insert(info)
	info2 = {"first_name" : first_name_var,"last_name" : last_name_var,"email" : email_stuff, "school" : school_name, "friendslist": DBRef(collection = "friends_list", id = original_id)}
	original_id_2=db.students.insert(info2)
	html = "<html><body> string: "+""+"</body></html>"

	

	#self.app.log.redirect_stdouts_to_logger(logger, rlevel)
	

@shared_task(name='module.tasks.mul')
def mul(x, y):
	print("DEBUG TEST")
	html = "<html><body> string: "+""+"</body></html>"
	return x + y


@shared_task
def xsum(numbers):
    return sum(numbers)