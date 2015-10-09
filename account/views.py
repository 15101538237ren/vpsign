# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from VPSign.helpers import *
from django.conf import settings
# Create your views here.

def index(request):
    return render_view_shortcut(request,"account","index")

#login 方法,get 返回登陆页,post返回index
@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return render_view_shortcut(request,"account","index")
        else:
            return render_view_shortcut(request,"account","login")
    elif request.method == "GET":
        if request.user.is_authenticated():
            return render_view_shortcut(request,"account","index")
        else:
            return render_view_shortcut(request,"account","login")
#login return json方法
@require_POST
def login_json(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    data={}
    if user is not None:
        auth.login(request, user)
        data = {"success":1,}
    else:
        data = {"success":0}
    return JsonResponse(data,safe=False)
