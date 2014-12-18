from django.conf.urls import patterns, url
from smsg.views import ListView, add, EditView

urlpatterns = patterns('',
   url(r'^$', ListView.as_view(), name='list'),
   url(r'^add/$', add, name='add'),
   url(r'^(?P<pk>\d+)/edit/$', EditView.as_view(), name='edit'),
)