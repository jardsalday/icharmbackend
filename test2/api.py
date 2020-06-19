from rest_framework import generics,permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer,RegisterSerializer,LoginSerializer,UserforAdminSerializer,ChangePasswordSerializer,UserProfileSerializer
from rest_framework import serializers
from rest_framework import viewsets
from django.contrib.auth.models import User 
from rest_framework.views import APIView
from .serializers import GetMedicUserProfileSerializer,RegisterUserSerializer,RegisterPatientUserSerializer,PatientUserProfileSerializer,GetPatientUserProfileSerializer
from .models import PatientUserProfile,MedicUserProfile
#Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })
#FORTESTING
class RegisterPatientAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    def update_profile(request,user_id):
        user = User.objects.get(id = '8')
        user.profile.position = 'Guard'
        user.save
    
        
#LoginAPI
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })

#Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UserForAdmin(viewsets.ModelViewSet):
    permission_classes =[
        permissions.AllowAny

    ]
    serializer_class = UserforAdminSerializer
    queryset = User.objects.all()

#UPDATE PASSWORD
class UpdatePassword(APIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (permissions.AllowAny, )
    def get_object(self):
        filter_1 = self.request.query_params.get('id','')
        return User.objects.filter(id='24')
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        old_password = serializer.data.get("old_password")
        filter1 = self.request.query_params.get('id','')
        u = User.objects.get(id=filter1)
        u.set_password(serializer.data.get("new_password"))
        u.save()
        return Response("Saved, You Handsome Man")
#REGISTER MEDICAL PRACTITIONER
class MedicUserViewSet(viewsets.ModelViewSet):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
#REGISTER PATIENT 
class PatientUserViewSet(viewsets.ModelViewSet):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    queryset = User.objects.all()
    serializer_class = RegisterPatientUserSerializer

class GetPatientViewSet(viewsets.ModelViewSet):
    permission_classes =[
        permissions.IsAuthenticated

    ]
    serializer_class = GetPatientUserProfileSerializer

    def get_queryset(self):
        return self.request.user.getpatients.all()

class SearchPatientViewSet(viewsets.ModelViewSet):
    permission_classes =[
        permissions.AllowAny

    ]
    serializer_class = GetPatientUserProfileSerializer
    
    def get_queryset(self):
        filter1 = self.request.query_params.get('name','1')
        return self.request.user.getpatients.all().filter(name__icontains=filter1)#.filter(name__iregex=r"[[:<:]]{0}[[:>:]]".format(filter1))

class GetAdminPatientViewSet(viewsets.ModelViewSet):
    permission_classes =[
        permissions.AllowAny

    ]
    serializer_class = GetPatientUserProfileSerializer
    queryset = PatientUserProfile.objects.all()
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)   
    # def get_queryset(self):
    #     filter1 = self.request.query_params.get('name','1')
    #     return PatientUserProfile.objects.all().filter(name__icontains=filter1)#.filter(name__iregex=r"[[:<:]]{0}[[:>:]]".format(filter1))
    
class SearchAdminPatientViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny] 
    serializer_class = GetPatientUserProfileSerializer  
    def get_queryset(self):
        filter1 = self.request.query_params.get('name','1')
        return PatientUserProfile.objects.all().filter(name__icontains=filter1)#.filter(name__iregex=r"[[:<:]]{0}[[:>:]]".format(filter1))
    
   
class GetMedicsViewSet(viewsets.ModelViewSet):
    permission_classes =[
        permissions.AllowAny

    ]
    serializer_class =UserProfileSerializer 

    def get_queryset(self):
        filter1 = self.request.query_params.get('name','1')
        return MedicUserProfile.objects.all().filter(name__icontains=filter1)#.filter(name__iregex=r"[[:<:]]{0}[[:>:]]".format(filter1)  )

class PatientViewSpecific(viewsets.ModelViewSet):
    permission_classes = [
         permissions.AllowAny

     ]
    serializer_class = GetPatientUserProfileSerializer
    def get_queryset(self):
        queryset = PatientUserProfile.objects.all()
        filter1 = self.request.query_params.get('id','')
        if filter1 is not None:
            queryset = queryset.filter(user_id=filter1)
        return queryset

class MedicViewSpecific(viewsets.ModelViewSet):
    permission_classes = [
         permissions.AllowAny

     ]
    serializer_class = GetMedicUserProfileSerializer
    def get_queryset(self):
        queryset = MedicUserProfile.objects.all()
        filter1 = self.request.query_params.get('id','')
        if filter1 is not None:
            queryset = queryset.filter(user_id=filter1)
        return queryset
class MedicForUser(viewsets.ModelViewSet):
    permission_classes = [
         permissions.AllowAny

     ]
    serializer_class = GetMedicUserProfileSerializer
    def get_queryset(self):
        queryset = MedicUserProfile.objects.all()
        filter1 = self.request.query_params.get('id','')
        if filter1 is not None:
            queryset = queryset.filter(user_id=filter1)
        return queryset   
class GetAdminMedicViewSet(viewsets.ModelViewSet):
    permission_classes =[
        permissions.AllowAny

    ]
    serializer_class = GetMedicUserProfileSerializer
    queryset = MedicUserProfile.objects.all() 
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)