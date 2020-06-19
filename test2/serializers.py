from rest_framework import serializers
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from .models import MedicUserProfile,PatientUserProfile


#UserSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','is_staff','username','email','is_superuser')
#UserforAdminSerializer
class UserforAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id','first_name','last_name','username','email','password')

#ChangePasswordForUserAdmin

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

#RegisterSerializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password':{'write_only':True}}
    
    def create(self,validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'] )
        return user


#LoginSerializer
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicUserProfile
        fields = ('user_id','name','email','birthdate','sex','address','position','hospital','email','phone_number')

class RegisterUserSerializer(serializers.ModelSerializer):
    medicprofile = UserProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'medicprofile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('medicprofile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_staff = True
        user.save()
        MedicUserProfile.objects.create(user=user,**profile_data,owner=self.context['request'].user)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('medicprofile')
        profile = instance.medicprofile

        instance.username = validated_data.get('username', instance.username)
        instance.save()
        
        profile.name = profile_data.get('name',profile.name)
        profile.birthdate = profile_data.get('birthdate',profile.birthdate)
        profile.sex = profile_data.get('sex',profile.sex)
        profile.address = profile_data.get('address',profile.address)
        profile.position = profile_data.get('position', profile.position)
        profile.hospital = profile_data.get('hospital', profile.hospital)
        profile.save()

        return instance


class PatientUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientUserProfile
        fields = ('id','name','birthdate','age','sex','address','height','is_dia','user_id','email','phone_number','smoker')

class GetPatientUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientUserProfile
        fields =  ('id','name','birthdate','age','sex','address','height','is_dia','user_id','owner_id','email','phone_number','smoker')
class GetMedicUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicUserProfile
        fields = ('id','user_id','name','birthdate','sex','address','position','hospital','phone_number','email')
class RegisterPatientUserSerializer(serializers.ModelSerializer):
    patientprofile = PatientUserProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'patientprofile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('patientprofile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        PatientUserProfile.objects.create(user=user,**profile_data,owner=self.context['request'].user,id=None)
        
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('patientprofile')
        profile = instance.patientprofile

        instance.username = validated_data.get('username', instance.username)
        instance.save()

        profile.name = profile_data.get('name',profile.name)
        profile.birthdate = profile_data.get('birthdate',profile.name)
        profile.sex = profile_data.get('sex',profile.sex)
        profile.address = profile_data.get('address',profile.address)
        profile.height = profile_data.get('height',profile.height)
        profile.is_dia = profile_data.get('is_dia',profile.is_dia)
        profile.save()

        return instance