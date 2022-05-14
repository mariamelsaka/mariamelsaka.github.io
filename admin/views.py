from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound
# Create your views here.

def admin_login(request):
    return render(request,"admin_login.html")

def add_podcast(request):
    return render(request,"add/add_podcast.html")

def add_admin(request):
    return render(request,"add/add_admin.html")

def add_video(request):
    return render(request,"add/add_video.html")



def admin_profile(request):
    return render(request,"admin_profile.html")

def dashboard(request):
    return render(request,"dashboard.html")