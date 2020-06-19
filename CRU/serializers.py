from rest_framework import serializers
from CRU.models import Patient,Measurement,Risk,Log,LogMeasure

#UserSerializer
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

# class AssessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assess
#         fields = '__all__'

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model =Measurement
        fields = '__all__'
   

class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Risk
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'

class LogMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogMeasure
        fields = '__all__'


