from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from views import list_all, view_one

urlpatterns = patterns('',
        url(r'^$', list_all, name='myprojects_list'),
        url(r'^(?P<slug>.*)/$', view_one, name='myprojects_view'),
        url(r'^type/(?P<slug>.*)$', view_one, name='myprojects_view_type'),
    )

# vim: et sw=4 sts=4
