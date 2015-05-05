from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import db_views
import json
import time


def login_view(request):
    """ return http for login page
    On POST check if the user exists and if so log them in.
    """
    if request.user.is_authenticated():
        return redirect("/dashboard")
    # If user is not posting, just return the page
    if not request.method == 'POST':
        return render(request, 'login.html')
    # Make a dict and add the username and password that was entered
    data = {}
    data['username'] = request.POST.get('email', False)
    data['password'] = request.POST.get('password', False)
    # See if user exists and is not active
    # user = User.objects.filter(username=data['username'])[0]
    # if not user.is_active:
    #     data['errors'] = "User " + + " is not active yet"
    #     return render(request, 'login.html', dictionary=data)
    # Try to login
    user = authenticate(username=data['username'], password=data['password'])
    if user is not None:
        # If login successful
        if user.is_active:
            # If the user has been approved
            login(request, user)
            return redirect("/dashboard")
            # Redirect to a success page.
        else:
            # If the user has not been approved
            data['errors'] = "The requested account has not been approved a socs admin"
            return render(request, 'login.html', dictionary=data)
            # Return a 'disabled account' error message
    else:
        # Failed login attempt
        # If they entered a username then print error
        if data['username'] != '':
            data['errors'] = "Username and password combination does not exist"
        return render(request, 'login.html', dictionary=data)
        # Return an 'invalid login' error message.

def find_school_ajax(request):
    data = {}
    data['email'] = request.user.username
    result = db_views.find_school(data)
    return HttpResponse(json.dumps(result), content_type="application/json")

@login_required(redirect_field_name='/login')
def delete_school_ajax(request):
    if 'Administrator' not in request.user.groups.values_list('name', flat=True):
        return None
    if not request.method == 'POST':
        return None
    data = {'school_name': request.POST.get('school_name'), 'school_address': request.POST.get('school_address')}
    result = db_views.delete_school(data)
    return HttpResponse(json.dumps(result), content_type="application/json")

@login_required(redirect_field_name='/login')
def delete_student_ajax(request):
    if 'Administrator' not in request.user.groups.values_list('name', flat=True):
        return None
    if not request.method == 'POST':
        return None
    data = {"email": request.POST.get('email')}
    db_views.delete_a_student_from_database(data)
    username = request.POST.get('student_email', False)
    return HttpResponse(content_type="application/json")



@login_required(redirect_field_name='/login')
def dashboard_view(request):
    """ render the admin dash if the user is logged in """
    if 'Administrator' in request.user.groups.values_list('name', flat=True):
        data = {}
        data['schools'] = db_views.get_all_schools()

        users = User.objects.filter(is_active=False)
        userRequests = []
        userRequests = db_views.get_people([user.username for user in users])
        data['users'] = userRequests

        active_accounts = User.objects.filter(is_active=True)
        print(active_accounts)
        print(" ")
        active_users = []
        active_users = db_views.get_people([active_acct.username for active_acct in active_accounts])
        print(active_users)
        active_users = filter(None, active_users)
        data['active_users'] = active_users
        print(active_users)
        return render(request, 'admin_dash.html', dictionary=data)
    return render(request, 'student_dash.html')

@login_required(redirect_field_name='/login')
def create_school_view(request):
    """ render the create school view. TODO: add validation """
    # Redirect if the user does not have admin rights
    if 'Administrator' not in request.user.groups.values_list('name',
                                                              flat=True):
        return redirect("/dashboard")
    # Display the create school view if the admin is logged in
    if request.method == 'GET':
        return render(request, 'create_school.html')
    elif request.method == 'POST':
        # TODO: Actually implement this-This is a copy of create user
        if request.POST.get("save"):
            # print(request.POST)
            is_valid, data = validate_new_school(request)
            # print(data)
            if is_valid:
                # Data is valid and let's store it in the db
                db_views.add_school_to_db(data)
                return redirect("/login")
            else:
                return render(request, 'create_user.html', dictionary=data)
        elif request.POST.get("cancel"):
            return redirect("/login")
        return render(request, 'create_user.html')


def validate_new_school(request):
    """ return (True if data is valid, Dictionary of input and errors)

    validate the school data that was entered in request
    """
    # TODO: Implement this-This is a copy of validate_new_user
    # Fill data with the information that the user entered
    data = create_school_data(request)
    valid_data = True
    # TODO: Validate the data-Right now we are just assuming it's correct
    # If any data is invalid, set valid_data to False and print error
#    if len(data['studName'].strip()) == 0:
#        valid_data = False
#        data['err_studName'] = "Please enter a name"
#    if validate_email(data['email']):
#        valid_data = False
#        data['err_email'] = "Invalid email"
#    if User.objects.filter(username=data['email']).count():
#        valid_data = False
#        data['err_email'] = "A user with that email already exists"
#    if len(data['school'].strip()) == 0:
#        valid_data = False
#        data['err_school'] = "Please enter a school"
#    if len(data['pw'].strip()) == 0:
#        valid_data = False
#        data['err_pw'] = "Please enter a password"
#    if not data['pw'] == data['conf_pw']:
#        valid_data = False
#        data['err_conf_pw'] = "Passwords didn't match"
    # Return if the valid
    return valid_data, data


def create_school_data(request):
    data = {}
    data['name'] = request.POST.get('name', False)
    data['address'] = request.POST.get('address', False)
    data['academicYear'] = request.POST.get('academicYear', False)
    data['daysInYear'] = int(request.POST.get('daysInYear', False))
    data['daysInASchedule'] = int(request.POST.get('daysInASchedule', False))
    data['semesterInYear'] = int(request.POST.get('semesterInYear', False))
    data['periodInDay'] = int(request.POST.get('periodInDay', False))
    # Parse the block information
    start_periods = request.POST.get('start_periods', False).split()
    end_periods = request.POST.get('end_periods', False).split()
    days_active = request.POST.get('days_active', False).split()
    block_info = []
    for i, item in enumerate(start_periods):
        block_info.append({'start': int(start_periods[i]),
                           'end': int(end_periods[i]),
                           'days_active': days_active[i].split(',')})
    data['block_info'] = block_info
    # Missing: semester=listofstrings and lunch=listofints
    # Find all the semesters added and lunches added
    data['semesters'] = []
    for i in range(int(data['semesterInYear'])):
        semester = request.POST.get('semester_' + str(i), False)
        if semester:
            data['semesters'].append(semester)
    data['lunches'] = []
    for i in range(int(data['periodInDay'])):
        lunch = request.POST.get('lunch_' + str(i), False)
        if lunch:
            data['lunches'].append(i+1)
    return data


def send_friend_request_ajax(request):
    data = {}
    data['email_of_sender'] = request.user.username

    info = db_views.get_a_person(request.user.username)
    # emailer = json_util.loads(name)
    name = json.loads(str(info))
    # print(name['first_name'])
    # print(name['last_name'])

    data['first_name_emailer'] = name['first_name']
    data['last_name'] = name['last_name']

    firstName = request.POST.get('first_name_emailee', False)
    lastName = request.POST.get('last_name_emailee', False)
    email = request.POST.get('email_of_sendee', False)

    data['email_of_sendee'] = email
    data['first_name_emailee'] = firstName
    data['last_name_emailee'] = lastName

    db_views.send_a_friend_request(data)
    return HttpResponse(json.dumps(data), content_type="application/json")

def add_class_to_database_ajax(request):
    data= {}
    data['username']=request.user.username
    data['course_id'] = request.POST.get('course_id', False)
    data['course_name'] = request.POST.get('course_name', False)
    data['instructor'] = request.POST.get('instructor', False)

    # data['school'] = ''
    # block = {'days_active': ['M','Tu'], 'end': 3, 'start': 0}
    # '0-3:M,Tu,W'
    block_text = request.POST.get('block', False).split(':')
    periods = block_text[0]
    days = block_text[1].split(',')
    start_period = periods.split('-')[0]
    end_period = periods.split('-')[1]
    # block = {'days_active': days, 'start': start_period,
    #          'end': end_period)
    data['days'] = days
    data['start_period'] = start_period
    data['end_period'] = end_period

    data['year'] = request.POST.get('year', False)
    data['semester'] = request.POST.get('semester', False)
    data['new_year_flag'] = False
    print(data)
    db_views.add_classes_to_database(data)
    return HttpResponse(json.dumps(data), content_type="application/json")

# def get_course_offering_ajax(request):
#     # print("test")
#     data= {}
#     data['username']=request.user.username
#     data['course_id'] = request.POST.get('course_id', False)
#     data['course_name'] = request.POST.get('course_name', False)
#     data['instructor'] = request.POST.get('instructor', False)
#     # data['school'] = ''
#     day = request.POST.get('days',False)
#     day = day.split(" ")
#     data['days'] = request.POST.get('days', False)
#     data['start_period']= request.POST.get('start_period', False)
#     data['end_period']= request.POST.get('end_period', False)
#     data['year'] = request.POST.get('year', False)
#     data['semester'] = request.POST.get('semester', False)
#     data['new_year_flag']=False

#     # data= {}
#     # email = data['email']
#     # year = data['year']

#     data = {}
#     data['email'] = request.user.username


#     db_views.add_classes_to_database(data)
#     return HttpResponse(json.dumps(data), content_type="application/json")

def get_assigned_schedule_ajax(request):
    data = {}
    data['email'] = request.user.username
    schedule = db_views.get_assigned_schedule(data)
    return HttpResponse(json.dumps(schedule), content_type="application/json")

def get_friend_ajax(request):
    data = {}
    data['email'] = request.user.username

    info = db_views.get_friends_list(data)

    return HttpResponse(json.dumps(info), content_type="application/json")

def get_friend_requests_ajax(request):
    data = {}
    data['email_of_sendee'] = request.user.username

    info = db_views.get_a_person(request.user.username)
    # emailer = json_util.loads(name)
    name = json.loads(str(info))

    data['first_name_emailee'] = name['first_name']
    data['last_name_emailee'] = name['last_name']

    info = db_views.get_friend_requests(data)
    #requests = json.loads(str(info))
    for person in info:
        del person['_id']
        del person['last_name_emailee']
        del person['email_of_emailee']
        del person['first_of_emailee']

    return HttpResponse(json.dumps(info), content_type="application/json")


def accept_friend_request_ajax(request):
    data = {}
    data['email_of_sendee'] = request.user.username
    data['email_of_requester'] = request.POST.get('email_of_requester', False)

    db_views.accept_friend_request(data)
    return HttpResponse(json.dumps(data), content_type="application/json")

def delete_friend_request_ajax(request):
    data = {}
    data['email_of_sendee'] = request.user.username
    data['email_of_requester'] = request.POST.get('email_of_requester', False)

    db_views.deny_friend_request(data)
    return HttpResponse(json.dumps(data), content_type="application/json")

def delete_friend_ajax(request):
    data = {}
    data['email'] = request.user.username
    data['first_name'] = request.POST.get('first_name', False)
    data['last_name'] = request.POST.get('last_name', False)
    data['friend_email'] = request.POST.get('friend_email', False)

    db_views.delete_friend_from_friends_list(data)
    return HttpResponse(json.dumps(data), content_type="application/json")

def create_user_view(request):
    """ GET: render the create new user form
    POST: validate the new user data and if valid submit to database
    """
    # Display the create user view
    if request.method == 'GET':
        return render(request, 'create_user.html')
    elif request.method == 'POST':
        if request.POST.get("request"):
            is_valid, data = validate_new_user(request)
            if is_valid:
                # Data is valid and let's store it in the db
                user = User.objects.create_user(username=data['email'],
                                                password=data['pw'])
                user.is_active = False
                user.save()
                db_views.add_student_entry(data)
                data["message"] = 'Welcome to our website! Please wait until you have been approved'
                data["message_sub"] = 'Welcome to SOCS'
                db_views.send_email_to_student(data)
                # db_views.add_students_to_database(data)
                return redirect("/login")
            else:
                return render(request, 'create_user.html', dictionary=data)
        elif request.POST.get("cancel"):
            return redirect("/login")
        return render(request, 'create_user.html')


def validate_new_user(request):
    """ return (True if data is valid, Dictionary of input and errors)

    validate the user data that was entered in request
    """
    # Fill data with the information that the user entered
    data = {}
    data['studName'] = request.POST.get('studName', False).strip().split()
    data['email'] = request.POST.get('email', False)
    data['school'] = request.POST.get('school', False)
    data['address'] = request.POST.get('address', False)
    data['pw'] = request.POST.get('password', False)
    data['conf_pw'] = request.POST.get('confirm', False)
    valid_data = True
    # If any data is invalid, set valid_data to False and print error
    if len(data['studName']) != 2:
        valid_data = False
        data['err_studName'] = "Please enter a valid name"
    else:
        data['first_name'] = data['studName'][0]
        data['last_name'] = data['studName'][1]
    if validate_email(data['email']):
        valid_data = False
        data['err_email'] = "Invalid email"
    if User.objects.filter(username=data['email']).count():
        valid_data = False
        data['err_email'] = "A user with that email already exists"
    if len(data['school'].strip()) == 0:
        valid_data = False
        data['err_school'] = "Please enter a school"
    if len(data['address'].strip()) == 0:
        valid_data = False
        data['err_address'] = "Please enter an address"
    if len(data['pw'].strip()) == 0:
        valid_data = False
        data['err_pw'] = "Please enter a password"
    if not data['pw'] == data['conf_pw']:
        valid_data = False
        data['err_conf_pw'] = "Passwords didn't match"
    # Return if the valid
    return valid_data, data


def validate_email(email):
    """ validate an email string """
    import re
    a = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if a.match(email):
        return False
    return True


def logout_view(request):
    """ log current user out """
    # Log the user out using Django Auth
    logout(request)
    return redirect("/login")


def redirect_to_login(request):
    """ redirect the user to login """
    # If you go to the homepage, redirect to login
    return redirect("/login")


@login_required(redirect_field_name='/login')
def friend_ajax(request):
    data = {'first_name': request.POST["first_name"]}
    data = db_views.get_possible_friends(request.user.username,
                                         request.POST["first_name"])

    return HttpResponse(json.dumps(data), content_type="application/json")

@login_required(redirect_field_name='/login')
def accept_student_request_ajax(request):
    if 'Administrator' not in request.user.groups.values_list('name',
                                                              flat=True):
        return redirect("/dashboard")
    # get username
    username = request.POST.get('student_email', False)
    user = User.objects.filter(username=username)[0]
    user.is_active = True
    data = {}
    data["email"] = username
    data["message"] = 'Your account has been approved'
    data["message_sub"] = 'Welcome to SOCS'
    db_views.send_email_to_student(data)
    user.save()
    return HttpResponse(content_type="application/json")

@login_required(redirect_field_name='/login')
def deny_student_request_ajax(request):
    if 'Administrator' not in request.user.groups.values_list('name',
                                                              flat=True):
        return redirect("/dashboard")
    # get username
    username = request.POST.get('student_email', False)
    user = User.objects.filter(username=username)[0]
    user.delete()
    return HttpResponse(content_type="application/json")

def get_course_offerings_ajax(request):
    data = {}
    data['email'] = request.user.username
    data['year'] = time.strftime("%Y")
    print(data['year'])
    courses = db_views.get_course_offerings(data)
    print(courses)
    return HttpResponse(json.dumps(courses), content_type="application/json")

def remove_assigned_course_ajax(request):
    data = {}
    data['email']= request.user.username
    data['course_name']=request.POST.get('course_name', False)
    data['start_period']= request.POST.get('start_period', False)
    data['end_period']= request.POST.get('end_period', False)
    data['course_id']= request.POST.get('course_id', False)
    data['instructor']= request.POST.get('instructor', False)
    days = request.POST.get('days_array', False)
    days = days.split(" ")
    days.remove("")
    data['days_array'] = days
    print(data)
    db_views.remove_a_class_from_assigned(data)
    print("it works")
    return HttpResponse(content_type="application/json")
