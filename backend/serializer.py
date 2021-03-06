from rest_framework import serializers
from .models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
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