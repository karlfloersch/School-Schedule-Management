from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


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
    """ render the admin dash if the user is logged in """
    if 'Administrator' in request.user.groups.values_list('name', flat=True):
        return render(request, 'admin_dash.html')
    return render(request, 'student_dash.html')


@login_required(redirect_field_name='/login')
def create_school_view(request):
    """ render the create school view. TODO: add validation """
    # Display the create school view if the admin is logged in
    if 'Administrator' in request.user.groups.values_list('name', flat=True):
        return render(request, 'create_school.html')
    return redirect("/dashboard")


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
                redirect("/login")
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
    data['studName'] = request.POST.get('studName', False)
    data['email'] = request.POST.get('email', False)
    data['school'] = request.POST.get('school', False)
    data['pw'] = request.POST.get('password', False)
    data['conf_pw'] = request.POST.get('confirm', False)
    valid_data = True
    # If any data is invalid, set valid_data to False and print error
    if len(data['studName'].strip()) == 0:
        valid_data = False
        data['err_studName'] = "Please enter a name"
    if validate_email(data['email']):
        valid_data = False
        data['err_email'] = "Invalid email"
    if len(data['school'].strip()) == 0:
        valid_data = False
        data['err_school'] = "Please enter a school"
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
