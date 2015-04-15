from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
import datetime
# import the logging library
import logging
# Testing
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)


def login_view(request):
    if request.user.is_authenticated():
        return redirect("/dashboard")
    # Create the data dictionary
    data = {}
    # Get the username and password that was entered
    data['username'] = request.POST.get('email', False)
    data['password'] = request.POST.get('password', False)
    # If none was entered, make sure the value is empty
    if not data['username']:
        data['username']=''
    if not data['password']:
        data['password']=''
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
            data['errors'] = "IM HEREJRIEWO"
            return render(request, 'login.html', dictionary=data)
            # Return a 'disabled account' error message
    else:
        # Failed login attempt
        # If they entered a username then print error
        if data['username'] != '':
            data['errors'] = "IM HEREJ"
        return render(request, 'login.html', dictionary=data)
        # Return an 'invalid login' error message.



@login_required(redirect_field_name='/login')
def dashboard_view(request):
    # Display the correct dashboard either student or admin
    if 'Administrator' in request.user.groups.values_list('name',flat=True):
        return render(request, 'admin_dash.html')
    return render(request, 'student_dash.html')


@login_required(redirect_field_name='/login')
def create_school_view(request):
    # Display the create school view if the admin is logged in
    if 'Administrator' in request.user.groups.values_list('name',flat=True):
        return render(request, 'create_school.html')
    return redirect("/dashboard")

def create_user_view(request):
    # Display the create user view
    if request.method == 'GET':
        return render(request, 'create_user.html')
    elif request.method == 'POST':
        if request.POST.get("request"):
            is_valid, data = validate_new_user(request)
            if is_valid:
                # Data is valid and let's store it in the db
                redirect("/login")
            else:
                return render(request, 'create_user.html', dictionary=data)
        elif request.POST.get("cancel"):
            return redirect("/login")
        return render(request, 'create_user.html')

def validate_new_user(request):
    data = {}
    data['studName'] = request.POST.get('studName', False)
    data['email'] = request.POST.get('email', False)
    data['school'] = request.POST.get('school', False)
    data['pw'] = request.POST.get('password', False)
    data['conf_pw'] = request.POST.get('confirm', False)
    valid_data = True
    if len(data['studName'].strip()) == 0:
        valid_data = False
        data['err_studName'] = "Invalid name"
    if validate_email(data['email']):
        valid_data = False
        data['err_email'] = "Invalid email"
    if len(data['school'].strip()) == 0:
        valid_data = False
        data['err_school'] = "Invalid school"
    if len(data['pw'].strip()) == 0:
        valid_data = False
        data['err_pw'] = "Invalid password"
    if data['pw'] == data['conf_pw']:
        valid_data = False
        data['err_conf_pw'] = "Passwords didn't match"
    return valid_data, data

def validate_email( email ):
    import re
    a = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if a.match(email):
        return False
    return True

def logout_view(request):
    # Log the user out using Django Auth
    logout(request)
    return redirect("/login")

def redirect_to_login(request):
    # If you go to the homepage, redirect to login
    return redirect("/login")
