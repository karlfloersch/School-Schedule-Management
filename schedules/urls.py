from django.conf.urls import patterns, url
from . import views, db_views

# Define the URLS that we are using
urlpatterns = patterns('',
	(r'^login/$', views.login_view), # Login page
    (r'^logout/$', views.logout_view), # Logout, redirect to login
    (r'^dashboard/$', views.dashboard_view), # Dash for user and admin
    (r'^create_school/$', views.create_school_view), # Create school for admin
    (r'^create_user/$', views.create_user_view), # New user request page
    (r'^sample_db_test/$', get_friendslist_view), # Testing for DB
    (r'^$', views.redirect_to_login), # Send user to login
)
