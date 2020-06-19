from django.urls import path, include
from .api import UpdatePatientView,MeasurementViewSet
from .apiPatient import LoginPatientAPI
from . import views
from . import api

urlpatterns=[
    
    # path('api/update/<pk>',UpdatePatientView.as_view()),
    path('patientmachine',views.patientmachine,name='patientmachine'),
    path('api/measures',views.measureList,name='measures'),
    # path('api/loginpat',LoginPatientAPI.as_view()),
    path('api/addmeasures',views.measures,name = 'addmeasures'),
    path('api/logdev',views.Logs,name= ' logdev'),
    path('api/logmeasure',views.LogMeasures,name='logmeasure'),
    path('api/logger',views.Logger,name='logger')
    

]