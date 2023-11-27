from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from .models import PatientProfile,DoctorProfile

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"hospital/index.html")
from django.shortcuts import get_object_or_404

def index(request):
    user = request.user

    # Check if the user is authenticated
    if user.is_authenticated:
        # Check if the user has a DoctorProfile with specialization
        is_doctor = DoctorProfile.objects.filter(user=user, specialization__isnull=False).exists()

        if is_doctor:
            doctor_profile = get_object_or_404(DoctorProfile, user=user)
            return render(request, "hospital/index.html", {"profile": doctor_profile, "user": user, "is_doctor": is_doctor})
        else:
            patient_profile = get_object_or_404(PatientProfile, user=user)
            return render(request, "hospital/index.html", {"profile": patient_profile, "user": user, "is_doctor": is_doctor})
    else:
        # Handle the case where the user is not authenticated (AnonymousUser)
        return render(request, "hospital/index.html")


def login_view(request):
    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if '@' in username:
            user = authenticate(request,username = User.objects.get(email = username),password = password)
            if user is not None:
            # User authentication was successful, log in the user
                login(request, user)
                return render(request, "hospital/index.html")  # Replace with the desired redirect after login
            else:
             # User authentication failed, provide an error message
                return render(request, "hospital/login.html", {"error_message": "Invalid username or password"})

        else:
            user = authenticate(request,username = username ,password = password)
            if user is not None:
            # User authentication was successful, log in the user
                login(request, user)
                return render(request, "hospital/index.html")  # Replace with the desired redirect after login
            else:
             # User authentication failed, provide an error message
                return render(request, "hospital/login.html", {"error_message": "Invalid username or password"})
    return render(request,"hospital/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register_p(request):
    if request.method == "POST":
        
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        image = request.FILES.get('profile_image')  #
        address = request.POST.get("address")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        state = request.POST.get("state")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 != password2:
            return render(request,"hospital/login.html",{
                "message":"password doesn't match"
            })
        
        try:
            user = User.objects.create_user(first_name = firstname,last_name = lastname, username = username, email = email, password = password1)
            user.save()
            patient = PatientProfile.objects.create(
                user = user,
                address_line1 = address,
                city = city,
                pincode = pincode,
                state = state
            )
            patient.profile_picture=image
            patient.save()
        except IntegrityError:
            return render(request, "hospital/register_p.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    else:
        return render(request, "hospital/register_p.html")        
    

def register_d(request):
    if request.method == "POST":
        
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        image = request.FILES.get('profile_image')
        specialization = request.POST.get("specialization")
        experienceyears = request.POST.get("experience_years")
        phone = request.POST.get("contact_number")
        licenseno = request.POST.get("license_number")
        address = request.POST.get("address")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        state = request.POST.get("state")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 != password2:
            return render(request,"hospital/login.html",{
                "message":"password doesn't match"
            })
        
        try:
            user = User.objects.create_user(first_name = firstname,last_name = lastname, username = username, email = email, password = password1)
            user.save()
            doctor = DoctorProfile.objects.create(
                user = user,
                specialization = specialization,
                experience_years = experienceyears,
                contact_number = phone,
                license_number = licenseno,
                address_line1 = address,
                city = city,
                pincode = pincode,
                state = state
            )
            doctor.profile_picture=image
            doctor.save()
        except IntegrityError:
            return render(request, "hospital/register_d.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    else:
        return render(request, "hospital/register_d.html") 