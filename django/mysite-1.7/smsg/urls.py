from django.conf.urls import patterns, url
from smsg.views import ListView, add

urlpatterns = patterns('',
   url(r'^$', ListView.as_view(), name='list'),
   url(r'^add/$', add, name='add'),
)