from django.conf.urls import patterns, url
from . import views, db_views, tasks

# Define the URLS that we are using
urlpatterns = patterns('',
	(r'^login/$', views.login_view), # Login page
    (r'^logout/$', views.logout_view), # Logout, redirect to login
    (r'^dashboard/$', views.dashboard_view), # Dash for user and admin
    (r'^dashboard/accept-student-account-request$', views.accept_student_request_ajax), # Accept a friend request
    (r'^dashboard/deny-student-account-request$', views.deny_student_request_ajax), # Delete a friend request
    (r'^dashboard/get-friends$', views.friend_ajax), # Dash for user and admin
    (r'^dashboard/send-friend-request$', views.send_friend_request_ajax), # Send friend request
    (r'^dashboard/delete-school$', views.delete_school_ajax), #delete school
    (r'^dashboard/delete-student$', views.delete_student_ajax), #delete a student from database
    (r'^dashboard/get-friends-request$', views.get_friend_requests_ajax), # Populate manage friend request
    (r'^dashboard/get-friends-schedules$', views.get_friends_schedules), # Populate manage friend request
    (r'^dashboard/get-school-info$', views.find_school_ajax), # Populate semester list
    (r'^dashboard/get-friend-list$', views.get_friend_ajax), # Populate manage friend
    (r'^dashboard/accept-friend-request$', views.accept_friend_request_ajax), # Accept a friend request
    (r'^dashboard/delete-friend-request$', views.delete_friend_request_ajax), # Delete a friend request
    (r'^dashboard/delete-friend$', views.delete_friend_ajax), # Delete a friend
    (r'^dashboard/add-assigned-class$', views.add_class_to_database_ajax), # add a class to the database
    (r'^dashboard/get-assigned-schedule$', views.get_assigned_schedule_ajax), # get the student's assigned schedule
    (r'^dashboard/get-course-offerings$', views.get_course_offerings_ajax), # get the course offerings of this year
    (r'^dashboard/remove-assigned-course$', views.remove_assigned_course_ajax), # remove a course from assigned schedule
    (r'^dashboard/export-course-schedule$', views.export_generated_ajax), # export course schedule to student
    (r'^dashboard/generate-course-schedule$', views.create_desired_schedule_ajax), # generate the course schedule
    (r'^create_school/$', views.create_school_view), # Create school for admin
    (r'^create_user/$', views.create_user_view), # New user request page
    (r'^sample_db_test/$', db_views.export_generated), # Testing for DB
    (r'^ta/$', db_views.test_cel),
    (r'^$', views.redirect_to_login), # Send user to login

)
