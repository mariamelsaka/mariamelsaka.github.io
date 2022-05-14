from django.shortcuts import render

# Create your views here.


def da7e7(request):
    return render(request, "creators/ahmed el3'andor.html")

def egychology(request):
    return render(request, "creators/ahmed samer.html")

def eman(request):
    return render(request, "creators/eman.html")

def home(request):
    return render(request, "home.html")

def profile(request):
    return render(request, "user_profile.html")

def login(request):
    return render(request, "auth/login.html")

def register(request):
    return render(request, "auth/sign-up.html")

def accounts_setting(request):
    return render(request, "accounts_setting.html")
