from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
  	url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
)