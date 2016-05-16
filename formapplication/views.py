from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
   return HttpResponse("Hello, this is  the index page")
def hello(request):
   return HttpResponse("Hello, this is the hello page")
