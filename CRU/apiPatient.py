from CRU.models import Patient,Measurement,Risk
from .serializers import PatientSerializer
from rest_framework import serializers
from rest_framework import generics,permissions
from django.http import HttpResponse,JsonResponse 
from django.contrib.auth import authenticate
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.authtoken.models import Token

class PatientLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model= Patient
        fields = ('username','password') 
    def validate(self,value):
        login_set = Patient.objects.all()
        sample = login_set.filter(username=value['username'],password=value['password'])
        if sample.count()>0:
            return value
        raise serializers.ValidationError("Incorrect Credentials")
        
        
class LoginPatientAPI(generics.GenericAPIView):
    serializer_class = PatientLoginSerializer
    def post(self, request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        return Response({
            "user":PatientLoginSerializer(user,context=self.get_serializer_context()).data
        })
        
    