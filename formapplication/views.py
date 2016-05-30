from django.http import Http404
from django.shortcuts import render, get_object_or_404
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
   patient = get_object_or_404(Patient, pk=patient_id)
   return render(request, 'formapplication/detail.html', {'patient': patient, 'allofthem': Patient.objects.all()})
def surname(request, patient_id):
   response="The patient your examining is %s"
   return HttpResponse(response%patient_id)
def firstname(request, patient_id):
   return HttpResponse("The firstname is %s"%patient_id)
