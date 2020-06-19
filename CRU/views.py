import numpy as np 
from .forms import ValidChol
import pickle
import pandas as pd
from django.shortcuts import render
from .models import Measurement,Patient,Log,LogMeasure
from test2.models import PatientUserProfile
from django.http import HttpResponse,JsonResponse
import urllib,json
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
import xgboost as xgb
import pickle
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier,GradientBoostingClassifier,AdaBoostClassifier

def patientmachine(request):
    array=[]

    x = urllib.request.urlopen('http://127.0.0.1:8000/api/measures?id=30')
    y = x.read()
    z = json.loads(y)
    for key in z:
        value = z[key]['sys']
        array.append(value)

        
    return HttpResponse(array)
# @api_view(["GET"])
# def jsonPatient(self):
#     patient_dict={}
#     patient_records=[]
#     test_set = Patient.objects.all()
#     for test in test_set:
#         tmp_id = test.id
#         tmp_name= test.name 
#         tmp_birthdate = test.birthdate 
#         tmp_sex = test.sex
#         tmp_address = test.address
#         tmp_height = test.height
#         tmp_diabetes = test.diabetes
#         tmp_created_at = test.created_at
#         record = {"id":tmp_id,"name":tmp_name,"birthdate":tmp_birthdate,"sex":tmp_sex,"height":tmp_height,"address":tmp_address,
#         "diabetes":tmp_diabetes,"created_at":tmp_created_at}
#         patient_records.append(record)
#     patient_dict = patient_records

#     return JsonResponse(patient_dict,safe = False)
# @api_view(['GET'])
# def searchPatient(request):
#     onePatient_dict = {}
#     onePatient_records = []
#     one_pat = Patient.objects.all()
#     filter_patient = request.GET['id']
#     if filter_patient is not None:
#         one_pat_ = one_pat.filter(id = filter_patient)
#     for test in one_pat_:
#         tmp_id = test.id
#         tmp_name= test.name 
#         tmp_birthdate = test.birthdate 
#         tmp_sex = test.sex
#         tmp_address = test.address
#         tmp_height = test.height
#         tmp_diabetes = test.diabetes
#         tmp_created_at = test.created_at
#         record = {"id":tmp_id,"name":tmp_name,"birthdate":tmp_birthdate,"sex":tmp_sex,"height":tmp_height,"address":tmp_address,
#         "diabetes":tmp_diabetes,"created_at":tmp_created_at}
#         onePatient_records.append(record)
#     onePatient_dict = onePatient_records
#     return JsonResponse(onePatient_dict,safe=False)
def measureList(request):
    measures_dict={}
    measures_record = []
    measures_set = Measurement.objects.all()
    filter_patient = request.GET['id']
    if filter_patient is not None:
        measures_set = measures_set.filter(id_number=filter_patient).order_by('-id')
    for x in measures_set:
        tmp_id = x.id_number
        tmp_sys = x.systolic
        tmp_pul = x.pulse
        tmp_weight = x.weight
        tmp_chol = x.cholesterol
        tmp_month = x.month
        tmp_day = x.day
        tmp_year = x.year
        tmp_nurse = x.nurse
        tmp_dia = x.dia
        tmp_age = x.age
        tmp_sex = x.sex
        tmp_diabetes =x.diabetes        
        records = {"id":tmp_id,"sys":tmp_sys,"pulse":tmp_pul,"weight":tmp_weight,"chol":tmp_chol,"month":tmp_month,"day":tmp_day,"year":tmp_year,
        "nurse":tmp_nurse,"dia":tmp_dia,"age":tmp_age,"sex":tmp_sex,"diabetes":tmp_diabetes}
        measures_record.append(records)
    measures_dict = measures_record
    return JsonResponse(measures_dict,safe=False) 
def Logs(request):   
    measures_dict={}
    measures_record = []

    log_set = Log.objects.all().order_by('-id') 
    for x in log_set:
        tmp_log = x.holder
        log = {"id":tmp_log}
        measures_record.append(log)
    measures_dict=measures_record
    return JsonResponse(measures_dict,safe = False)    
def Logger(request):
    log = request.GET["log"]
    logger = Log(holder = log)
    logger.save()
    return HttpResponse(log)
def LogMeasures(request):   
    measures_dict={}
    measures_record = []
    log_set = LogMeasure.objects.all().order_by('-id') 
    for x in log_set:
        tmp_log = x.sugar
        log = {"id":tmp_log}
        measures_record.append(log)
    measures_dict=measures_record
    return JsonResponse(measures_dict,safe = False)    



#   id_number = models.CharField(max_length=100)
#     age = models.CharField(max_length=100)
#     systolic= models.CharField(max_length=100)
#     height = models.CharField(max_length=100)
#     weight= models.CharField(max_length=100)
#     cholesterol = models.CharField(max_length=100)
#     glucose = models.CharField(max_length=100)
#     smoke = models.CharField(max_length=100)
#     birthdate = models.CharField(max_length=100)
#     created_at = models.CharField(max_length=100)

# @api_view(["POST"])
# def cvdpred(request):
#     try:
#         df = pd.read_csv("C:/Users/Lenovo T420/Downloads/iCHARM/Cardio3.csv")
#         df =df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]
#         GradBost = GradientBoostingClassifier(random_state = 15)
#         x=df.iloc[:,0:6]
#         y=df.iloc[:,-1]
#         x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 37)
#         GradBost.fit(x_train,y_train)
#         X= pd.read_csv("C:/Users/Lenovo T420/Downloads/iCHARM/pangtesting.csv")
#         x_semis=X.iloc[:,0:6]
#         mydata = request.data
#         unit = np.array(list(mydata.values()))
#         unit = unit.reshape(1,-1)
#         y_pred = GradBost.predict_proba(unit)[:,1]
#         return JsonResponse('Your prediction is {}'.format(y_pred[0]),safe=False)
#     except ValueError as e:
#         return HttpResponse("HEllo")

# @api_view(["POST"])
# def test(request):
#     form = ValidChol(request.POST or None)
#     if form.is_valid():
#         form.save()
    
#     return Response(form)
# Create your views here.
#  stng = "https://capstoneproxycardio.herokuapp.com/addmeasures.php?id=" + str(mtake) + "&sys=" + str(tbSys.value) + "&dia=" + str(tbDia.value) + "&pulse=" + str(tbPul.value) + "&weight=" + str(tbWei.value) + "&chol=" + str(tbChol.value) + "&created_at=" + theDate + "&nurse=" + str(nurses) + "&name=" + str(names) + "&age=" + str(ages) + "&sex=" + str(sexs)
   
def measures(request):
    id_number = request.GET["id"]
    systolic = request.GET["sys"]
    diastolic =request.GET["dia"]
    pulse = request.GET["pulse"]
    weight = request.GET["weight"]
    cholesterol = request.GET["chol"]
    BMI = request.GET["BMI"]
    month = request.GET["month"]
    day = request.GET["day"]
    year = request.GET["year"]
    nurse = request.GET["nurse"]
    age = request.GET["age"]
    sex = request.GET["sex"]
    smoker = request.GET["smoke"]
    glucose = request.GET["glucose"]
    created_at = month + "/"+day+"/"+year
    pseudo = "temp"
    real_gluc = ''
    real_chol = ''
    real_smoke = ''
    
    print(systolic)
    if smoker =="1":
        real_smoke = "1"
    else:
        real_smoke = "0"
    
    if int(cholesterol)>200 and int(cholesterol)<240:
        real_chol = "1"
    elif int(cholesterol)>240 and int(cholesterol)<=300:
        real_chol = "1"
    else:
        real_chol = "0"
    
    if glucose =="3" and real_chol =="3":
        real_gluc = "1"
    elif glucose =="3" and real_chol =="2":
        real_gluc = "1"
    elif glucose =="3" and real_chol=="1":
        real_gluc = "1"
    else:
        real_gluc="0"
    # from sklearn.externals import joblib
    array = {"ageyears":age,"bmi":BMI,"systolic":systolic,'diastolic':diastolic,"smoker":real_smoke,"diabetes":real_gluc,"cholesterol":real_chol}
    print(array)
    # mdl = joblib.load()
    with open('C:/Users/jjmai/Desktop/Cardio 547,652020/testing/test1/CRU/model_jmaiii_version','rb') as f:
        model = pickle.load(f)
    single = np.array([int(age),int(BMI),int(systolic),int(diastolic),int(real_smoke),int(real_gluc),int(real_chol)])
    single_pred = pd.DataFrame(single)
    final = single_pred.transpose()
    final.columns = ['ageyears','bmi','systolic','diastolic','smoke','diabetes','cholesterol']
    y_pred_proba = model.predict_proba(final)
    y_pred = model.predict(final)
    print(y_pred_proba)
    print(y_pred_proba[0][0],y_pred_proba[0][1])
    
    proba0 = y_pred_proba[0][0]*100.0    
    proba1 =y_pred_proba[0][1]*100.0 
    rounded_proba0 = round(proba0)
    rounded_proba1 = round(proba1)
    
    
    measurements = Measurement(id_number = id_number,risk=y_pred[0],risk_proba1=rounded_proba1,risk_proba0=rounded_proba0, owner_id=id_number,systolic=systolic,diastolic=diastolic,BMI = BMI,weight=weight,cholesterol=cholesterol,month=month,day=day,year=year,nurse = nurse,age = age,sex = sex,height=pseudo,glucose=glucose,birthdate=pseudo,dia=pseudo,pulse = pulse,diabetes=glucose,created_at=created_at,smoke=real_smoke)
    measurements.save()
    print("proba0:"+str(proba0),"proba1"+str(proba1),"label:"+str(2))
    log = {"proba0":str(proba0),"proba1":str(proba1),"label":str(y_pred)}
    pred_dict={}
    pred_record = []
    pred_record.append(log)
    pred_dict=pred_record
    return JsonResponse(pred_dict,safe=False)
    # df = pd.read_csv("C:/Users/Lenovo T420/Downloads/iCHARM/PseudoFinal2.csv")
    # df =df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]
    # xgb = XGBClassifier(learning_rate=0.5,n_estimators=500,random_state=7,gamma=5,min_child_weight=10,max_depth=10)
    # x=df.iloc[:,0:6]
    # y=df.iloc[:,-1]
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 37)
    # xgb.fit(x_train,y_train)
    # file_name = 'XGB_tuned_final.pkl'
    # joblib.dump(xgb,file_name)
    # print(joblib.dump)

   
    
    # y_pred = xgb.predict(final)
    # print(proba,y_pred)
    # measurements = Measurement(id_number = id_number,risk=y_pred,risk_proba=proba, owner_id=id_number,systolic=systolic,diastolic=diastolic,weight=weight,cholesterol=cholesterol,month=month,day=day,year=year,nurse = nurse,age = age,sex = sex,height=pseudo,glucose=glucose,smoke=pseudo,birthdate=pseudo,dia=pseudo,pulse = pulse,diabetes=glucose,created_at=created_at,smoker=real_smoke)
    # measurements.save()
    # try:
    #     array={"age":age,"BMI":weight,"ap_hi":systolic,"cholesterol":real_chol,
    #              "gluc":real_gluc,"smoke":"1"}
    #     df = pd.read_csv("C:/Users/Lenovo T420/Downloads/iCHARM/Cardio3.csv")
    #     df =df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]
    #     GradBost = GradientBoostingClassifier(random_state = 15)
    #     x=df.iloc[:,0:6]
    #     y=df.iloc[:,-1]
    #     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 37)
    #     GradBost.fit(x_train,y_train)
    #     unit = np.array(list(array.values()))
    #     unit = unit.reshape(1,-1)
    #     y_pred = GradBost.predict_proba(unit)[:,1]
    #     y_pred1 = GradBost.predict(unit)
    #     #return JsonResponse('Your prediction is {}'.format(y_pred[0]),safe=False)
    #     measurements = Measurement(id_number = id_number,risk=y_pred,risk_proba=y_pred_proba, owner_id=id_number,systolic=systolic,diastolic=diastolic,weight=weight,cholesterol=cholesterol,month=month,day=day,year=year,nurse = nurse,age = age,sex = sex,height=pseudo,glucose=glucose,smoke=pseudo,birthdate=pseudo,dia=pseudo,pulse = pulse,diabetes=glucose,created_at=created_at,smoker=real_smoke)
    #     measurements.save()
    # return render(request, 'Measures.html')