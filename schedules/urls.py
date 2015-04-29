from django.conf.urls import patterns, url
from . import views, db_views, tasks

# Define the URLS that we are using
urlpatterns = patterns('',
	(r'^login/$', views.login_view), # Login page
    (r'^logout/$', views.logout_view), # Logout, redirect to login
    (r'^dashboard/$', views.dashboard_view), # Dash for user and admin
    (r'^dashboard/get-friends$', views.friend_ajax), # Dash for user and admin
    (r'^dashboard/send-friend-request$', views.send_friend_request_ajax), # Send friend request
    (r'^dashboard/get-friends-request$', views.get_friend_requests_ajax), # Populate manage friend request
    (r'^dashboard/accept-friend-request$', views.accept_friend_request_ajax), # Accept a friend request   
    (r'^create_school/$', views.create_school_view), # Create school for admin
    (r'^create_user/$', views.create_user_view), # New user request page
    (r'^sample_db_test/$', db_views.get_a_person), # Testing for DB
    (r'^ta/$', db_views.test_cel),
    (r'^$', views.redirect_to_login), # Send user to login

)
