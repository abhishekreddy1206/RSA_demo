from django.conf.urls import patterns, include, url
import views
import api
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',

    url(r'^$', views.index),
    url(r'^confirm$', views.confirm),

    url(r'^api/register/$', api.RegistrationList.as_view()),
    url(r'^api/register/(?P<pk>\d+)$', api.RegistrationDetails.as_view())
)
