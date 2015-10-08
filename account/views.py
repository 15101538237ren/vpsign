from django.shortcuts import render

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from VPSign.helpers import *
# Create your views here.

def index(request):
    return render_to_response('account/index.html', locals(), context_instance=RequestContext(request))
@require_POST
def login(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
    else:
        return JsonResponse()
def logout(request):
    logout(request)