from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class MedicUserProfile(models.Model):
    user = models.OneToOneField(User,related_name='medicprofile',on_delete=models.CASCADE)
    owner = models.ForeignKey(User,related_name="getmedics",on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    birthdate = models.CharField(max_length =100)
    sex = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    age = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    # position = models.CharField(max_length=100)
    # hospital = models.CharField(max_length=100) 
    def __str__(self):
        return self.name

class PatientUserProfile(models.Model):
    user = models.OneToOneField(User,related_name="patientprofile",on_delete=models.CASCADE)
    owner = models.ForeignKey(User,related_name="getpatients",on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,unique=True)
    birthdate = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    is_dia = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    smoker = models.CharField(max_length=100)
    def __str__(self):
        return self.name
