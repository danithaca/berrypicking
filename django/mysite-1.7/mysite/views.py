from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.http import HttpResponse
import json
from django.template.response import TemplateResponse
import sys


def home(request):
    return TemplateResponse(request, 'mysite/home.jinja2', context={
        'title': 'Homepage',
        'version': sys.version
    })
    #return HttpResponse("hello, %s" % str(request.user))
    #return login(request)