from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class Caregiver_skillsserializer(serializers.ModelSerializer):
    class Meta:
        model = Caregiver_skills
        fields = '__all__'
class Caregiver_serviceserializer(serializers.ModelSerializer):
    class Meta:
        model = Caregiver_service
        fields = '__all__'
class Worksserializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = '__all__'
class Schoolserializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
class Jobsserializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
class Applicantsserializer(serializers.ModelSerializer):
    class Meta:
        model = Applicants
        fields = '__all__'
class Availabilityserializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'
class Job_serviceserializer(serializers.ModelSerializer):
    class Meta:
        model = Job_service
        fields = '__all__'
class Locationsserializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'
class Skillsserializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
class Servicesserializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class Userserializer(serializers.ModelSerializer):
    userservices = Caregiver_serviceserializer(read_only=True, many=True)
    userskills = Caregiver_skillsserializer(read_only=True, many=True)
    def create(self, validated_data):
        user =  User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            location_id=validated_data['location_id'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            legal_id=validated_data['legal_id'],
            caregiver=validated_data['caregiver'],
            adress=validated_data['adress'],
            phone=validated_data['phone'],
        )
        return user
    class Meta:
        model = User
        fields = '__all__'