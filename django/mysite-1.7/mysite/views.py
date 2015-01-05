from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.core.mail import send_mail
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


def demo(request):
    send_mail('Greetings %s' % request.user.get_username(), 'test message', from_email='danithaca@gmail.com', recipient_list=('mrzhou@umich.edu',))