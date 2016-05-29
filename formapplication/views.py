from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Patient
def index(request):
   the_patients_list = Patient.objects.order_by('-id')[:2]   
   context = {
	'the_patients_list':the_patients_list,
   }
   return render(request, 'formapplication/index.html', context)
def hello(request):
   return HttpResponse("Hello, this is the hello page")
def detail(request, patient_id):
   return HttpResponse("This is patient number %s"%patient_id)
def surname(request, patient_id):
   response="The patient your examining is %s"
   return HttpResponse(response%patient_id)
def firstname(request, patient_id):
   return HttpResponse("The firstname is %s"%patient_id)
