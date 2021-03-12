from django.shortcuts import render
from backend.models import *
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets, generics
from backend.serializer import *
from django.urls import reverse_lazy, resolve, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html')

#class UserViewSet(generics.ListCreateAPIView):
#    serializer_class = Userserializer
#    queryset = User.objects.all()
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = Userserializer
    queryset = User.objects.all()

    #permission_classes = (IsAuthenticated,)
    #authentication_class = (TokenAuthentication,)

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
    serializer_class = Jobsserializer
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

class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    #success_url = 'api/v1/user/'
    success_url = reverse_lazy('api:user_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        userin = authenticate(username = form.cleaned_data['username'],
        password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = userin)
        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)

class Logout(APIView):
    def get(self, request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)
