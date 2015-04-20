from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from celery.result import AsyncResult
import pymongo
import json
from schedules.tasks import *
from celery import Celery
from pymongo import MongoClient
from bson.dbref import DBRef
from django.http import HttpResponse
from . import tasks
client = MongoClient()
import time


def get_possible_friends(username, first_name):
    taskObject_from_task = possible_friends.delay(username,
                                                  first_name)
    result = check_task(taskObject_from_task.task_id)
    return result


@login_required(redirect_field_name='/login')
def add_a_student_to_friendslist_view(request):
    db = client.students
    username = request.user.username
    myself = db.students.find_one({"email": username})
    original_id = myself["_id"]
    first_name_to_be_inserted = "punk"
    last_name_to_be_inserted = "bitch"
    email_to_be_inserted = "punk@gmail.com"
    db.friends_list.update(
        {"_id": original_id},
        {"$push":
         {"list":
          {"first_name": first_name_to_be_inserted, "last_name":
           last_name_to_be_inserted, "email": email_to_be_inserted}}})
    html = "<html><body> string: "+"success"+"</body></html>"
    return HttpResponse(html)


@login_required(redirect_field_name='/login')
def add_school_to_db(data):
	# def add_school_to_db(data):
	# THIS IS DUMMY DATA
	name_of_school = "larz school of balance"
	days_in_a_year = 40
	number_of_sem = 3
	address = "20 monkie ave."
	num_days_in_a_schedule = 5
	num_periods_in_a_day = 5
	#dictionary {nameofsemester}
	name_of_semesters=["fall","winter","spring"]
	#must be bundled with year
	#dictionary
	# lunch_periods = data['luch_periods']
	# legal_blocks = data['legal_blockname_of_semesters,s']
	blocks1={'start': 3,'end': 4,'days_active':['monday','tuesday','thursday']}
	blocks2={'start': 2,'end': 3,'days_active':['monday','tuesday','friday']}
	blocks3={'start': 1,'end': 4,'days_active':['tuesday','thursday']}
	year_name = "2014"
	course_listing_and_semster = []

	#for x in range len(name_of_semesters)
		#course_listing_and_semster += {None, name_of_semesters[x]} 

	year = {'year_name':year_name,'num_periods_in_a_day':num_periods_in_a_day,
	'blocks':[blocks1, blocks2, blocks3],
	'semesters':course_listing_and_semster}

	data= {'semester_names':name_of_semesters,'name':name_of_school, 'num_days':days_in_a_year, 'num_sem':number_of_sem, 'address':address, 'num_days_in_schedule':num_days_in_a_schedule, 'year_obj':year}

	taskObject_from_task = add_school_to_database_two.delay(data)
	result = check_task_http(taskObject_from_task.task_id)

	return result


def check_task_http(request):
    async_result = AsyncResult(request)
    try:
        result = async_result.get(timeout=30, propagate=False)
    except TimeoutError:
        result = None
    status = async_result.status
    traceback = async_result.traceback
    if isinstance(result, Exception):
        return HttpResponse(json.dumps({
            'status': status,
            'error': str(result),
            'traceback': traceback,
        }), content_type='application/json')
    else:
        return HttpResponse(json.dumps({
            'status': status,
            'result': str(result),
        }), content_type='application/json')


def check_task(request):
    async_result = AsyncResult(request)
    try:
        result = async_result.get(timeout=30, propagate=False)
    except TimeoutError:
        result = None
    status = async_result.status
    traceback = async_result.traceback
    if isinstance(result, Exception):
        return json.dumps({'status': status, 'error': str(result),
                           'traceback': traceback})
    else:
        return result


def test_cel(request):
    print ("Supa Duba")
    # html = add_students_to_database.apply_sync
    # html = tasks.mul.apply_async((2,2))
    # task_id = request.POST.get('tasl_')
    taskObject_from_task = add_students_to_database_two.delay()
    result = check_task_http(taskObject_from_task.task_id)

    #html = taskObject_from_task.get()
    # result.get()
    #task_id = result.task_id
    #print (result.ready())
    #print (result.status())

    #result = app.AsyncResult(task_id)
    #task_id = result.task_id

    # print (result.state)
    # result.state
    # print (results.state)

    #page = result.get()
    # print(page)

    #html = AsyncResult(task_id)
    #html = "<html><body> string: "+str(result)+"</body></html>"
    return result


def add_student_entry(data):
    #html = add_students_to_database.apply_sync
    # html = tasks.mul.apply_async((2,2))
    #task_id = request.POST.get('tasl_')
    taskObject_from_task = add_students_to_database_two.delay(data)
    result = check_task_http(taskObject_from_task.task_id)

    #html = taskObject_from_task.get()
    # result.get()
    #task_id = result.task_id
    #print (result.ready())
    #print (result.status())

    #result = app.AsyncResult(task_id)
    #task_id = result.task_id

    # print (result.state)
    # result.state
    # print (results.state)

    #page = result.get()
    # print(page)

    #html = AsyncResult(task_id)
    #html = "<html><body> string: "+str(result)+"</body></html>"
    return result


def send_a_friend_request_view(request):
    db = client.students
    email_of_requester = "billy@gmail.com"
    first_name_of_requester = "billy"
    last_name_of_requester = "bob"
    email_of_emailee = "charles@gmail.com"
    name_of_emailee = "charles"
    friend_request_info = {"email_of_requester": email_of_requester,
                           "first_name_of_requester": first_name_of_requester,
                           "last_name_of_requester": last_name_of_requester,
                           "email_of_emailee": email_of_emailee,
                           "name_of_emailee": name_of_emailee}
    db.friend_requests.insert_one(friend_request_info)

    html = "<html><body> string: "+"success"+"</body></html>"
    return HttpResponse(html)


def get_friendslist_view(request):
    db = client.students
    # dat_base_var = "students"
    first_name_var = "billy"
    last_name_var = "bob"
    email_stuff = "billy@gmail.com"
    school_name = "magic school bus"
    info = {
        "first_name": first_name_var,
        "last_name": last_name_var,
        "list": []}
    original_id = db.friends_list.insert(info)
    info2 = {
        "first_name": first_name_var,
        "last_name": last_name_var,
        "email": email_stuff,
        "school": school_name,
        "friendslist": DBRef(
            collection="friends_list",
            id=original_id)}
    # original_id_2=db.students.insert(info2)
    db.students.insert(info2)
    html = "<html><body> string: "+""+"</body></html>"
    return HttpResponse(html)
