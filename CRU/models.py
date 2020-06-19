from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from rest_framework import serializers


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE,null =True)
    name = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=100)
    sex = models.CharField(max_length =100)
    address = models.CharField(max_length = 100)
    height = models.CharField(max_length = 100)
    owner = models.ForeignKey(User,related_name="patients",on_delete=models.CASCADE,null = True)
    created_at = models.DateTimeField(auto_now_add = True)    
    diabetes = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name



# class Assess(models.Model):
#     patient_number = models.CharField(max_length=100)
#     complaints = models.CharField(max_length=100)
#     assessment1 = models.CharField(max_length=500)
#     prescriptions = models.CharField(max_length=500)
#     owner = models.ForeignKey(Patient,related_name="assess",on_delete=models.CASCADE,null = True)

class Measurement(models.Model):
    id_number = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    systolic= models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight= models.CharField(max_length=100)
    cholesterol = models.CharField(max_length=100)
    glucose = models.CharField(max_length=100)
    smoke = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    nurse = models.CharField(max_length=100)
    BMI = models.CharField(max_length=100)
    diastolic = models.CharField(max_length=100)
    dia = models.CharField(max_length=100)
    pulse = models.CharField(max_length=100)
    diabetes = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    risk = models.CharField(max_length=100, null = True)
    risk_proba1 = models.CharField(max_length=100, null=True)
    risk_proba0 = models.CharField(max_length=100,null=True)
    created_at = models.CharField(max_length=100,null=True)
    owner = models.ForeignKey(User,related_name="measurepatient",on_delete=models.CASCADE,null = True)
   
    
class Risk(models.Model):
    id_number = models.CharField(max_length= 100)
    risk = models.CharField(max_length=100)
    risk_proba = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)

class Log(models.Model):
    holder = models.CharField(max_length=100)

class LogMeasure(models.Model):
    sugar = models.CharField(max_length=100)
    