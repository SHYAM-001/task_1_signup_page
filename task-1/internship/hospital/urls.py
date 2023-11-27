from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout"),
    path("register/Patient",views.register_p,name="register_p"),
    path("register/Doctor",views.register_d,name="register_d"),
]
