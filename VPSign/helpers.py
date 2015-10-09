__author__ = 'ren'
import os
from django.http import HttpResponse, JsonResponse
import simplejson as json
from mappers import *
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

def error_response(error, **kwargs):
	code, message = error_mapping[error]
	return JsonResponse({"code": code, "message": message.format(**kwargs)})

def success_response(response=None):
	return JsonResponse({"code": 0, "message": response})

def ajax_required(func):
	def __decorator(request, *args, **kwargs):
		if request.is_ajax:
			return func(request, *args, **kwargs)
		else:
			raise ApiError("ONLY_FOR_AJAX")
	return __decorator

class ApiError(Exception):
	def __init__(self, key, **kwargs):
		Exception.__init__(self)
		self.key = key if key in error_mapping else "UNKNOWN"
		self.kwargs = kwargs

def render_view_shortcut(request,module,name):
    return render_to_response(module+"/"+name+".html", locals(), context_instance=RequestContext(request))