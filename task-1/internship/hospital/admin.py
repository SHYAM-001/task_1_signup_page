from django.contrib import admin
from .models import PatientProfile,DoctorProfile
# Register your models here.
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)