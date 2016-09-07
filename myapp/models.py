from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Depart(models.Model):
	id = models.IntegerField(primary_key=True)
	dept_name = models.CharField(max_length = 200)

class Staff(models.Model):
	id = models.IntegerField(primary_key=True)
	fname = models.CharField(max_length=200, blank=True)
	lname = models.CharField(max_length=200, blank=True)
	email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
	home_add = models.CharField(max_length=200, blank=True)
	depart = models.ForeignKey(Depart, on_delete=models.CASCADE, null=True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    	phone_number = models.CharField(max_length = 15,validators=[phone_regex], blank=True) # validators should be a list

def save(self, *args, **kwargs):
    if self.email is not None and self.email.strip() == "":
        self.email = None
    models.Model.save(self, *args, **kwargs)

def __str__(self):
	return ''.join([self.fname, self.lname,])


	