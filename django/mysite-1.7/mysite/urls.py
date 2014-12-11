from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django.template.response.TemplateResponse', {'template': 'mysite/home.html', 'context': {'message': 'hello foobar'}}, name='home'),
    #url(r'^$', 'mysite.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'extra_context': {'next': '/'}}, name='login'),
    #url(r'^user/', include('django.contrib.auth.urls', namespace="user")),

    # url(r'^blog/', include('blog.urls')),

    # this has to be set in order for django to direct to polls.urls.py
    url(r'^polls/', include('polls.urls', namespace="polls")),

    url(r'^admin/', include(admin.site.urls)),
)
