from django.conf.urls import patterns, include, url
from . import views
app_name = 'formapplication'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^hello/', views.hello, name = 'hello'),
    url(r'^(?P<patient_id>[1-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<patient_id>[1-9]+)/surname/$', views.surname, name='surname'),
    url(r'^(?P<patient_id>[1-9]+)/firstname/$', views.firstname, name='firstname'),
]
