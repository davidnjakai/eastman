from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', 'formapplication.views.index', name = 'index'),
    url(r'^hello/', 'formapplication.views.hello', name = 'hello')
]
