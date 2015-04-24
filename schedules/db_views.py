from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from celery.result import AsyncResult
import pymongo
import json
from bson import json_util,ObjectId
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

# Unfinished
@login_required(redirect_field_name='/login')
def add_classes_to_database(request):
    # Course ID     Course Name     Instructor  School  Days    Period Start    Period End
    data= {}
    data['username']=request.user.username
    data['course_id'] = 'cse306'
    data['course_name'] = 'operating systems'
    data['instructor'] = 'stark'
    # data['school'] = ''
    data['days'] = ['tues','thurs']
    data['start_period']='2'
    data['end_period']='3'
    data['year']='2015'
    data['semester']='fall'
    data['new_year_flag']=False

    taskObject_from_task = add_classes_to_database_two.delay(data)
    result = check_task(taskObject_from_task.task_id)
    html = "<html><body> string: "+"good JOb"+"</body></html>"
    return HttpResponse(html)





# @login_required(redirect_field_name='/login')
# def add_a_student_to_friendslist_view(request):
#     db = client.students
#     username = request.user.username
#     myself = db.students.find_one({"email": username})
#     original_id = myself["_id"]
#     first_name_to_be_inserted = "punk"
#     last_name_to_be_inserted = "bitch"
#     email_to_be_inserted = "punk@gmail.com"
#     db.friends_list.update(
#         {"_id": original_id},
#         {"$push":
#          {"list":
#           {"first_name": first_name_to_be_inserted, "last_name":
#            last_name_to_be_inserted, "email": email_to_be_inserted}}})
#     html = "<html><body> string: "+"success"+"</body></html>"
#     return HttpResponse(html)


def edit_school_to_database(request):
    address_of_edit = data['address_of_edit']
    name_of_school = data['name']
    days_in_a_year = data['daysInYear']
    number_of_sem = data['semesterInYear']
    address = data['address']
    num_days_in_a_schedule = data['daysInASchedule']
    num_periods_in_a_day = data['periodInDay']
    #dictionary {nameofsemester}
    name_of_semesters=data['semesters']
    blocks =data['block_info']
    year_name = data['academicYear']
    course_listing_and_semster = []
    lunches = data['lunches']
    year = {'year_name':year_name,'num_periods_in_a_day':num_periods_in_a_day,'blocks':blocks,
    'semesters':course_listing_and_semster}

    data= {'semester_names':name_of_semesters,'name':name_of_school, 'num_days':days_in_a_year, 'num_sem':number_of_sem, 'address':address, 'num_days_in_schedule':num_days_in_a_schedule, 'year_obj':year, 'lunches': lunches}

    taskObject_from_task = edit_school_to_database_two.delay(data,address_of_edit)
    result = check_task_http(taskObject_from_task.task_id)

    return result

def add_school_to_db(data):
    name_of_school = data['name']
    days_in_a_year = data['daysInYear']
    number_of_sem = data['semesterInYear']
    address = data['address']
    num_days_in_a_schedule = data['daysInASchedule']
    num_periods_in_a_day = data['periodInDay']
    #dictionary {nameofsemester}
    name_of_semesters=data['semesters']
    #must be bundled with year
    #dictionary
    # lunch_periods = data['luch_periods']
    # legal_blocks = data['legal_blockname_of_semesters,s']
    # blocks1={'start': 3,'end': 4,'days_active':['monday','tuesday','thursday']}
    # blocks2={'start': 2,'end': 3,'days_active':['monday','tuesday','friday']}
    # blocks3={'start': 1,'end': 4,'days_active':['tuesday','thursday']}
    blocks =data['block_info']
    year_name = data['academicYear']
    course_listing_and_semster = []
    lunches = data['lunches']

    #for x in range len(name_of_semesters)
        #course_listing_and_semster += {None, name_of_semesters[x]} 

    year = {'year_name':year_name,'num_periods_in_a_day':num_periods_in_a_day,
    'blocks':blocks,
    'semesters':course_listing_and_semster}

    data= {'semester_names':name_of_semesters,'name':name_of_school, 'num_days':days_in_a_year, 'num_sem':number_of_sem, 'address':address, 'num_days_in_schedule':num_days_in_a_schedule, 'year_obj':year, 'lunches': lunches}

    taskObject_from_task = add_school_to_database_two.delay(data)
    result = check_task_http(taskObject_from_task.task_id)

    return result


@login_required(redirect_field_name='/login')
def get_schools_view(request):
    data= {}
    data['school_name'] = 'larz school of balance'
    taskObject_from_task = search_school_from_database_two.delay(data)
    result = check_task(taskObject_from_task.task_id)
    # results['name']
    result2 = json_util.loads(result)

    # Front end modify to your hearts content
    this_school = result2[0]
    name_of_this_school = this_school['name']
    html = "<html><body> string: "+str(name_of_this_school)+"</body></html>"
    return HttpResponse(html)
    # return str(result2[0])   

# not done
@login_required(redirect_field_name='/login')
def get_schools_address_view(request):
    data= {}
    data['school_name'] = 'larz school of balance'
    data['address'] = 'place holder'
    taskObject_from_task = get_schools_address_two.delay(data)
    result = check_task(taskObject_from_task.task_id)
    # results['name']
    result2 = json_util.loads(result)

    # Front end modify to your hearts content
    this_school = result2[0]
    name_of_this_school = this_school['name']
    html = "<html><body> string: "+str(name_of_this_school)+"</body></html>"
    return HttpResponse(html)
    # return str(result2[0])   



@login_required(redirect_field_name='/login')
def get_all_students_view(request):
    taskObject_from_task = search_all_students_two.delay()
    result = check_task(taskObject_from_task.task_id)
    result2 = json_util.loads(result)

    this_student= result2[0]
    name_of_this_student = this_student['first_name']
    html = "<html><body> string: "+str(name_of_this_student)+"</body></html>"
    return HttpResponse(html)


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


def send_a_friend_request(request):

    data = {}
    # "first_name" : "ray",
    # "last_name" : "bill",
    # "friendslist" : DBRef("friends_list", ObjectId("5535f5b7cb99257cfaca4c25")),
    # "school" : "rays school of choice",
    # "address" : "ray ave",
    # "email" : "ray@gmail.com"

    # "_id" : ObjectId("5535e3accb99256b2c1c4899"),
    # "first_name" : "cheap",
    # "last_name" : "will",
    # "friendslist" : DBRef("friends_list", ObjectId("5535e3accb99256b2c1c4898")),
    # "school" : "cheap school",
    # "address" : "cheap ave",
    # "email" : "cheap@gmail.com"
    
    #ray is sender
    #cheap is sendee

    data['email_of_sender']='ray@gmail.com'
    data['first_name_emailer']='ray'
    data['last_name']='bill'
    data['email_of_sendee']='bill@gmail.com'
    data['first_name_emailee']='bill'
    data['last_name_emailee']='ray'


    taskObject_from_task = send_a_friend_request_two.delay(data)
    result = check_task_http(taskObject_from_task.task_id)
    html = "<html><body> string: "+"success"+"</body></html>"
    return HttpResponse(html)




def accept_friend_request(request):
    data = {}

    # "email_of_requester" : "ray@gmail.com"

    data['email_of_sendee']="bill@gmail.com"
    data['email_of_requester']="ray@gmail.com"

    taskObject_from_task = accept_friend_request_two.delay(data)
    result = check_task(taskObject_from_task.task_id)
    html = "<html><body> string: "+"success"+"</body></html>"
    return HttpResponse(html)
    # data[]



def deny_friend_request(request):
    data = {}
    data['email_of_sendee']="cheap@gmail.com"
    data['email_of_requester']="ray@gmail.com"

    taskObject_from_task = deny_friend_request_two.delay(data)
    result = check_task(taskObject_from_task.task_id)
    html = "<html><body> string: "+"success"+"</body></html>"
    return HttpResponse(html)


def get_friend_requests(request):
    data = {}
    data['email_of_sendee']="cheap@gmail.com"
    data['first_name_emailee']='cheap'
    data['last_name_emailee']='will'

    # "email_of_emailee" : "cheap@gmail.com",
    # "last_name_emailee" : "will",
    # "first_of_emailee" : "cheap",

    taskObject_from_task = get_friend_request_two.delay(data)
    result = check_task(taskObject_from_task.task_id)
    result2 = json_util.loads(result)
    particular_res = result2[0]

    val = particular_res['email_of_requester']
    # print(val)
    html = "<html><body> string: "+"success"+"</body></html>"
    return HttpResponse(html)

def delete_friend_from_friends_list(request):
    data = {}
    data['email'] = "ray@gmail.com"
    data['first_name'] = "bill"
    data['last_name'] = "ray"
    data['friend_email'] = "bill@gmail.com"
    taskObject_from_task = delete_friend_from_friends_list_two.delay(data)
    result = check_task(taskObject_from_task.task_id)
    html = "<html><body> string: "+"success"+"</body></html>"
    return HttpResponse(html)



def get_friends_list(request):
    data = {}
    data['email']='ray@gmail.com'
    taskObject_from_task = get_friends_list_two.delay(data)
    result = check_task(taskObject_from_task.task_id)
    print(result[0])
    result = result[0]
    print(result['first_name'])
    html = "<html><body> string: "+"success"+"</body></html>"
    return HttpResponse(html)