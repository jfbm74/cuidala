from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Locations(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Skills(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return str(self.id)

class Services(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return str(self.id)

class User(AbstractUser):
    legal_id=models.CharField(max_length=15)
    caregiver=models.BooleanField(default=False)
    patient=models.BooleanField(default=False)
    adress=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    updated_at=models.DateTimeField(default=datetime.now, blank=True)
    location_id=models.ForeignKey(Locations, on_delete=models.CASCADE, default=1)
    photo=models.ImageField(blank=True)
    def __str__(self):
        return str(self.id)

class Caregiver_service(models.Model):
    service_id=models.ForeignKey(Services, on_delete=models.CASCADE)
    caregiver_id=models.ForeignKey(User, related_name="userservices", on_delete=models.CASCADE)

class Caregiver_skills(models.Model):
    skill_id=models.ForeignKey(Skills, on_delete=models.CASCADE)
    caregiver_id=models.ForeignKey(User, related_name="userskills", on_delete=models.CASCADE)

class Works(models.Model):
    employer=models.CharField(max_length=30)
    work_title=models.CharField(max_length=30)
    start_date=models.DateTimeField(auto_now=True)
    end_date=models.DateTimeField(auto_created=True)
    job_description=models.CharField(max_length=150)
    location_id=models.ForeignKey(Locations, on_delete=models.CASCADE)
    caregiver_id=models.ForeignKey(User, on_delete=models.CASCADE)

class School(models.Model):
    name=models.CharField(max_length=50)
    study=models.CharField(max_length=30)
    start_date=models.DateTimeField(auto_created=True)
    end_date=models.DateTimeField(auto_created=True)
    caregiver_id=models.ForeignKey(User, on_delete=models.CASCADE)
    location_id=models.ForeignKey(Locations, on_delete=models.CASCADE)

class Jobs(models.Model):
    the_type=models.ForeignKey(Services, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_created=True)
    start_date=models.DateTimeField(auto_created=True)
    end_date=models.DateTimeField(auto_created=True)
    patient_phone=models.CharField(max_length=20)
    patient_age=models.IntegerField()
    patient_id=models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    salary_start=models.IntegerField()
    salary_end=models.IntegerField(blank=True)
    status=models.CharField(max_length=20)
    updated_at=models.DateTimeField(auto_now_add=True)
    location_id=models.ForeignKey(Locations, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Applicants(models.Model):
    job_id=models.ForeignKey(Jobs, on_delete=models.CASCADE)
    caregiver_offer=models.IntegerField()
    patient_offer=models.IntegerField()
    status=models.CharField(max_length=15)
    created_at=models.DateTimeField(auto_created=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    caregiver_id=models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class Availability(models.Model):
    job_id=models.ForeignKey(Jobs, on_delete=models.CASCADE)
    morning=models.BooleanField()
    afternoon=models.BooleanField()
    night=models.BooleanField()
    days=models.CharField(max_length=60)

class Job_service(models.Model):
    job_id=models.ForeignKey(Jobs, on_delete=models.CASCADE)
    service_id=models.ForeignKey(Services, on_delete=models.CASCADE)