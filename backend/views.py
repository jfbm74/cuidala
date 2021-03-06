from django.shortcuts import render
from Database.models import *
from django.http import HttpResponse
from rest_framework import viewsets
from Database.serializer import *

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = Userserializer
    queryset = User.objects.all()
class Caregiver_skillsViewSet(viewsets.ModelViewSet):
    serializer_class = Caregiver_skillsserializer
    queryset = Caregiver_skills.objects.all()
class Caregiver_serviceViewSet(viewsets.ModelViewSet):
    serializer_class = Caregiver_serviceserializer
    queryset = Caregiver_service.objects.all()
class WorksViewSet(viewsets.ModelViewSet):
    serializer_class = Worksserializer
    queryset = Works.objects.all()
class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = Schoolserializer
    queryset = School.objects.all()
class JobsViewSet(viewsets.ModelViewSet):
    serializer_class = Job_serviceserializer
    queryset = Jobs.objects.all()
class ApplicantsViewSet(viewsets.ModelViewSet):
    serializer_class = Applicantsserializer
    queryset = Applicants.objects.all()
class AvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = Availabilityserializer
    queryset = Availability.objects.all()
class Job_serviceViewSet(viewsets.ModelViewSet):
    serializer_class = Job_serviceserializer
    queryset = Job_service.objects.all()
class LocationsViewSet(viewsets.ModelViewSet):
    serializer_class = Locationsserializer
    queryset = Locations.objects.all()
class SkillsViewSet(viewsets.ModelViewSet):
    serializer_class = Skillsserializer
    queryset = Skills.objects.all()
class ServicesViewSet(viewsets.ModelViewSet):
    serializer_class = Servicesserializer
    queryset = Services.objects.all()