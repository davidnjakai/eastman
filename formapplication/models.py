from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patient(models.Model):
	lastname = models.CharField(max_length=45)
	firstname = models.CharField(max_length=45)
	middlename = models.CharField(max_length=45)
	title = models.CharField(max_length=45)
	mobilenumber = models.CharField(max_length=45)
	mobilenumber2 = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	guarantor = models.IntegerField(default=0)
	dateofbirth = models.DateField(auto_now=False, auto_now_add=False)
	filenumber = models.IntegerField(default=0)
	photolocation = models.CharField(max_length=45)
	gender = models.CharField(max_length=10)
	position = models.CharField(max_length=10)
	dueamount = models.IntegerField(default=0)
	insuranceamount = models.IntegerField(default=0)
	balancedue = models.IntegerField(default=0)
	occupation = models.CharField(max_length=45)
	employer_school = models.CharField(max_length=45)
	def __str__(self):
		return self.lastname