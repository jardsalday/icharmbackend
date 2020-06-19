from django.http import HttpResponse,JsonResponse   
import numpy as np 
import pandas as pd
# from sklearn.externals import joblib
from CRU.models import Patient,Measurement,Risk,Log,LogMeasure
from rest_framework import viewsets,permissions,generics
from .serializers import LogSerializer,PatientSerializer,MeasurementSerializer,RiskSerializer,LogMeasureSerializer
from rest_framework.generics import RetrieveAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
# from sklearn.ensemble import RandomForestClassifier,BaggingClassifier,GradientBoostingClassifier,AdaBoostClassifier
import numpy as np 
# from sklearn.model_selection import train_test_split
import pandas as pd
import json
class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated

     ]
    serializer_class=PatientSerializer

    def get_queryset(self):
        return self.request.user.patients.all()
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)
    def perform_update(self,serializer):
        serializer.save(owner = self.request.user)
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class MeasurementUser(viewsets.ModelViewSet):
    permissions_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class = MeasurementSerializer
    def get_queryset(self):
        return self.request.user.measurepatient.all()
class GetSpecificMeasureViewSet(viewsets.ModelViewSet):
    permission_classes = [
         permissions.AllowAny

     ]
    serializer_class = MeasurementSerializer
    def get_queryset(self):
        queryset = Measurement.objects.all()
        filter1 = self.request.query_params.get('id_number','')
        if filter1 is not None:
            queryset = queryset.filter(id_number=filter1)
        return queryset
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
class GetSpecificRiskViewSet(viewsets.ModelViewSet):
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class = RiskSerializer
    def get_queryset(self):
        queryset = Risk.objects.all()
        filter1 = self.request.query_params.get('id_number','')
        if filter1 is not None:
            queryset = queryset.filter(id_number=filter1)
        return queryset
class UpdatePatientView(UpdateAPIView):
    permission_classes = [
         permissions.IsAuthenticated
     ]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# class AssessViewSet(viewsets.ModelViewSet):
#     permission_classes = [
#          permissions.IsAuthenticated

#      ]
#     serializer_class=AssessSerializer
#     def get_queryset(self):
#         queryset = Assess.objects.all()
# #         filter1 = self.request.query_params.get('patient_number','')
# #         if filter1 is not None:
# #              queryset = queryset.filter(patient_number=filter1)
# #         return queryset

class MeasurementViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny

    ]
    queryset = Measurement.objects.all() 
    serializer_class=MeasurementSerializer
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    # def perform_create(self,serializer):
    #     array={"age":serializer.validated_data['birthdate'],"BMI":serializer.validated_data['weight'],"ap_hi":serializer.validated_data['systolic'],"cholesterol":serializer.validated_data['cholesterol'],
    #             "gluc":"1","smoke":"1"}
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
    #     r = Risk( id_number ="12",risk = y_pred1[0],risk_proba = str(y_pred[0]),created_at = "models.CharField(max_length=100))")
    #     r.save()
    #     serializer.save()    

class RiskViewSet(viewsets.ModelViewSet):
    permissions_classes = [

        permissions.AllowAny
    ]
    serializer_class = RiskSerializer
    queryset = Risk.objects.all()

class LogViewSet(viewsets.ModelViewSet):
    permissions_classes=[

        permissions.AllowAny

    ]
    serializer_class  = LogSerializer
    queryset = Log.objects.all()

class LogMeasureSet(viewsets.ModelViewSet):
    permissions_classes=[
        permissions.AllowAny
    ]
    serializer_class = LogMeasureSerializer
    queryset = LogMeasure.objects.all()