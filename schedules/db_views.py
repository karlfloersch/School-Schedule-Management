from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required(redirect_field_name='/login')
def sample_vew(request):
    """ render the create school view. TODO: add validation """
    # Display the create school view if the admin is logged in
    if 'Administrator' in request.user.groups.values_list('name', flat=True):
        return render(request, 'create_school.html')
    return redirect("/dashboard")

