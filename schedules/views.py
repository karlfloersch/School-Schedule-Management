from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group

# Create your views here.
from django.http import HttpResponse
import datetime

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
            return redirect("/dashboard")
            # Redirect to a success page.
        else:
            form['errors'] = "IM HEREJRIEWO"
            return render(request, 'login.html', dictionary=form)
            # Return a 'disabled account' error message
    else:
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
