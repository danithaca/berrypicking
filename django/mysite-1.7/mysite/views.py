from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.http import HttpResponse
import json
from django.template.response import TemplateResponse


def home(request):
    return TemplateResponse(request, 'mysite/index.html', context={
        'message': 'hello foobar'
    })
    #return HttpResponse("hello, %s" % str(request.user))
    #return login(request)