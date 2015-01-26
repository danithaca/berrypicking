from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import settings
from crop import views

urlpatterns = patterns('',

    url(r'^view/(?P<pk>\d+)/$', views.ProfileView.as_view(), name='view'),
    url(r'^$', views.dummy, name='home'),
    url(r'^edit/(?P<pk>\d+)/$', views.EditView.as_view(), name='edit'),

    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
