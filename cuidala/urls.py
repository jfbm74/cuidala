"""cuidala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backend import views
from rest_framework.routers import DefaultRouter
from backend.views import *
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'api/v1/user', UserViewSet, basename="userun")
router.register(r'api/v1/caregiver_skills', Caregiver_skillsViewSet)
router.register(r'api/v1/caregiver_service', Caregiver_serviceViewSet)
router.register(r'api/v1/works', WorksViewSet)
router.register(r'api/v1/school', SchoolViewSet)
router.register(r'api/v1/jobs', JobsViewSet)
router.register(r'api/v1/applicants', ApplicantsViewSet)
router.register(r'api/v1/availability', AvailabilityViewSet)
router.register(r'api/v1/job_service', Job_serviceViewSet)
router.register(r'api/v1/locations', LocationsViewSet)
router.register(r'api/v1/skills', SkillsViewSet)
router.register(r'api/v1/services', ServicesViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('token/', views.obtain_auth_token),
    path('login/', Login.as_view(), name = 'login'),
    path('theuser/', include(('backend.urls', 'api'))),
    path('logout/', Logout.as_view()),
    path('tokens/', views.obtain_auth_token),

]
