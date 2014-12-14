from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'django.template.response.TemplateResponse', {'template': 'mysite/home.jinja2', 'context': {'message': 'hello foobar'}}, name='home'),
    url(r'^$', 'mysite.views.home', name='home'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'extra_context': {'next': '/'}, 'template_name': 'mysite/login.jinja2'}, name='login'),
    # no need to set 'next' if LOGIN_REDIRECT_URL is set to /
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'mysite/login.jinja2'}, name='login'),
    #url(r'^user/', include('django.contrib.auth.urls', namespace="user")),

    # url(r'^blog/', include('blog.urls')),

    # this has to be set in order for django to direct to polls.urls.py
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^smsg/', include('smsg.urls', namespace="smsg")),

    url(r'^admin/', include(admin.site.urls)),
)
