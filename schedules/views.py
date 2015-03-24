from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
import datetime
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def login_view(request):
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
            logger.info('User: ' + data['username'] + ' logged in')
            return redirect("/dashboard")
            # Redirect to a success page.
        else:
            # If the user has not been approved
            data['errors'] = "IM HEREJRIEWO"
            return render(request, 'login.html', dictionary=data)
            # Return a 'disabled account' error message
    else:
        # Failed login attempt
        logger.info('Failed login attempt. Username: ' 
            + data['username'] + ' | Password: ' + data['password'])
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
    return render(request, 'create_user.html')

def logout_view(request):
    # Log the user out using Django Auth
    logout(request)
    return redirect("/login")

def redirect_to_login(request):
    # If you go to the homepage, redirect to login
    return redirect("/login")