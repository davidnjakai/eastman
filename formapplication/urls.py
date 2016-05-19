from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^hello/', views.hello, name = 'hello'),
    url(r'^(?P<patient_id>[1-2]+)/$', views.detail, name='detail'),
    url(r'^(?P<patient_id>[1-2]+)/surname/$', views.surname, name='surname'),
    url(r'^(?P<patient_id>[1-2]+)/firstname/$', views.firstname, name='firstname'),
]
