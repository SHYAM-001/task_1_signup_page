from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    profile_picture = models.ImageField(
        upload_to='profile_pics',
        blank=True,
        null=True,
        default="Profile_pics/default.jpg",
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    
    def __str__(self):
        return self.user.username

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField(blank=True)
    contact_number = models.IntegerField(blank=True)
    license_number = models.CharField(max_length=50, null=True, blank=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    
    def __str__(self):
        return self.user.username
