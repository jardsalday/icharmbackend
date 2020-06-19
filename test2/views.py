from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import MedicUserProfile,PatientUserProfile
from django.http import HttpResponse,JsonResponse
# Create your views here.
@api_view(["GET"])
def jsonPatient(self):
    patient_dict={}
    patient_records=[]
    test_set = PatientUserProfile.objects.all().order_by('-id')
    for test in test_set:
        tmp_id = test.user_id
        tmp_name= test.name 
        tmp_birthdate = test.birthdate 
        tmp_sex = test.sex
        tmp_address = test.address
        tmp_height = test.height
        tmp_diabetes = test.is_dia
        tmp_created_at = test.created_at
        tmp_smoker = test.smoker
        tmp_age = test.age
        record = {"id":tmp_id,"name":tmp_name,"age":tmp_age,"birthdate":tmp_birthdate,"sex":tmp_sex,"height":tmp_height,"address":tmp_address,
        "diabetes":tmp_diabetes,"smoker":tmp_smoker,"created_at":tmp_created_at}
        patient_records.append(record)
    patient_dict = patient_records

    return JsonResponse(patient_dict,safe = False)
@api_view(['GET'])
def searchPatient(request):
    onePatient_dict = {}
    onePatient_records = []
    one_pat = PatientUserProfile.objects.all()
    filter_patient = request.GET['name']
    if filter_patient is not None:
        one_pat_ = one_pat.filter(name__icontains=filter_patient)
    for test in one_pat_:
        tmp_id = test.user_id
        tmp_name= test.name 
        tmp_birthdate = test.birthdate 
        tmp_sex = test.sex
        tmp_address = test.address
        tmp_height = test.height
        tmp_diabetes = test.is_dia
        tmp_created_at = test.created_at
        tmp_smoker = test.smoker
        tmp_age = test.age
        record = {"id":tmp_id,"name":tmp_name,"age":tmp_age,"birthdate":tmp_birthdate,"sex":tmp_sex,"height":tmp_height,"address":tmp_address,
        "diabetes":tmp_diabetes,"smoker":tmp_smoker,"created_at":tmp_created_at}
        onePatient_records.append(record)
    onePatient_dict = onePatient_records
    return JsonResponse(onePatient_dict,safe=False)
def measureList(request):
    measures_dict={}
    measures_record = []
    measures_set = Measurement.objects.all()
    filter_patient = request.GET['id']
    if filter_patient is not None:
        measures_set = measures_set.filter(id=filter_patient).order_by('-id')
    for x in measures_set:
        tmp_id = x.id
        tmp_sys = x.systolic
        tmp_pul = x.pulse
        tmp_weight = x.weight
        tmp_chol = x.cholesterol
        tmp_month = x.month
        tmp_day = x.day
        tmp_year = x.year
        tmp_nurse = x.nurse
        tmp_dia = x.dia
        tmp_name = x.name
        tmp_age = x.age
        tmp_sex = x.sex
        tmp_diabetes:x.diabetes
        records = {"id":tmp_id,"sys":tmp_sys,"pulse":tmp_pul,"weight":tmp_weight,"chol":tmp_chol,"month":tmp_month,"day":tmp_day,"year":tmp_year,
        "nurse":tmp_nurse,"dia":tmp_dia,"name":tmp_name,"age":tmp_age,"sex":tmp_sex,"diabetes":tmp_diabetes}
        measures_record.append(records)
    measures_dict = measures_record
    return JsonResponse(measures_dict,safe=False)