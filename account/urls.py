from django.conf.urls import patterns, include, url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
  	url(r'^login$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/account/login'} ,name="logout"),
)