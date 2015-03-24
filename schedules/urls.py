from django.conf.urls import patterns, url
from . import views
urlpatterns = patterns('',
	(r'^login/$', views.login_view),
    (r'^logout/$', views.logout_view),
    (r'^dashboard/$', views.dashboard_view),
    (r'^create_school/$', views.create_school_view),
    (r'^create_user/$', views.create_user_view),
)