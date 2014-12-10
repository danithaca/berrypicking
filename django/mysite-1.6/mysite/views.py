from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.http import HttpResponse
import json


def home(request):
    return HttpResponse("hello, %s" % str(request.user))
    #return login(request)