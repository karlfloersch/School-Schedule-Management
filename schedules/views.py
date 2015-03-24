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
    form = {}
    form['username'] = request.POST.get('email', False)
    form['password'] = request.POST.get('password', False)
    if not form['username']:
        form['username']=''
    if not form['password']:
        form['password']=''
    user = authenticate(username=form['username'], password=form['password'])
    if user is not None:
        if user.is_active:
            login(request, user)
            logger.info('User: ' + form['username'] + ' logged in')
            return redirect("/dashboard")
            # Redirect to a success page.
        else:
            form['errors'] = "IM HEREJRIEWO"
            return render(request, 'login.html', dictionary=form)
            # Return a 'disabled account' error message
    else:
        logger.info('Failed login attempt. Username: ' + form['username'] + ' | Password: ' + form['password'])
        form['errors'] = "IM HEREJ"
        return render(request, 'login.html', dictionary=form)
        # Return an 'invalid login' error message.



@login_required(redirect_field_name='/login')
def dashboard_view(request):
    if 'Administrator' in request.user.groups.values_list('name',flat=True):
        return render(request, 'admin_dash.html')
    return render(request, 'student_dash.html')


@login_required(redirect_field_name='/login')
def create_school_view(request):
    if 'Administrator' in request.user.groups.values_list('name',flat=True):
        return render(request, 'create_school.html')
    return redirect("/dashboard")

def create_user_view(request):
    return render(request, 'create_user.html')

def logout_view(request):
    logout(request)
    return redirect("/login")