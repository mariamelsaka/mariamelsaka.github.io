from django.shortcuts import render,redirect
from django.http import HttpResponse ,HttpResponseNotFound, HttpResponseRedirect
from .models import customAdmins
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Videos,ContentCreators
from django.db import models

# Create your views here.

def admin_login(request):
      if request.method=="POST":
            username= request.POST['username']
            password= request.POST['password']
            user= auth.authenticate(username=username,password=password)
            if user is not None:
              auth.login(request, user)
              return redirect('admin_profile')
            else:
              messages.info(request,'invalid username or password')
              return redirect('admin_login')
      else:
         return render(request,'admin_login.html')



def admin_login(request):
    return render(request,"admin_login.html")


def error(request):
    return render(request,"error.html")



# VIDEOS--------------------------------------------
def create(request):
    return render(request, 'add/add_video.html')

def add_video(request):
    if request.method == "POST":
        title = request.POST['title']  
        description=request.POST['description']
        video_url=request.POST['video_url'] 
        content_creator_name=request.POST['content_creator_name']
        views=request.POST['views']
        video=Videos.objects.create(title=title,description=description,video_url=video_url,content_creator_name=content_creator_name,views=views)
        video.save()
        return redirect('show_video')
    else:
        return redirect('error')

def show_videos(request):
    return render(request, "edit/show_video_content.html",{'videos':Videos.objects.all()})




def show_specific(request, id):
    # Function to show a single post
    
    # START CODE HERE
    # 1- Get post by id
    video = Videos.objects.get(video_id=id)
    
    # 2- Create the context
    context = {
        'video': video
    }
    # 3- return template 'posts/show.html' with context
    return render(request,'edit/show_specific_video.html', context)
    # END CODE



def update_video(request, id):
    # Function to update a row of existing video
    if request.method == "POST":
        # check that request method is PUT
        _method = request.POST['_method'].upper()
        if _method == "PUT":
            video = Videos.objects.get(video_id=id)

            # check that video exists
            if video is not None:
                # Recieve new data & Update post
                title=request.POST['title']
                description=request.POST['description']
                
            # Update video values
            # video=Videos.objects.update(title=title, description=description)
                video.title = title
                video.description = description

                # Apply the update to the database
                video.save()
                

                context = {
                    'video' : video,
                    'alert' : {
                        'type' : 'success',
                        'message' : 'Your post is updated successfully.'
                    }
                    }
                return render(request, 'edit/show_specific_video.html', context)
            else:
                # video is not found
                return render(request, 'error.html')
        else:
            # request method is not PUT
            return redirect('error.html')
    else:
        # request method is not POST
        return redirect('error.html')



def delete_video(request, id):
    # Function to delete existing post
    if request.method == 'POST':
        _method = request.POST['_method'].upper()
        if _method == "DELETE":
            # Init context & retrieve video
            

            # Find video by id
            video= Videos.objects.get(video_id=id)

            # if video exists -> delete it
            if video is not None:

                # Delete video
                video.delete()
                
                redirect("show_video")
                
            else:
                # video is not found
                return render(request, 'error.html')
        else:
            # request method is not DELETE
            return redirect('error.html')
    else:
        # request method is not POST
        return redirect('error.html')
    
    
# CONTENT CREATORS-----------------------------

# def show_content_creators(request):
#     return render(request,"edit/show_content_creators.html")

def create_content_creators(request):
    return render(request, 'add/add_content.html')

def add_content(request):
    if request.method == "POST":
        name = request.POST['name']  
        description=request.POST['description']
        content=ContentCreators.objects.create(name=name,description=description)
        content.save()
        return redirect('show_content_creators')
    else:
        return redirect('error')


def show_content_creators(request):
    return render(request, "edit/show_content_creators.html",{'ContentCreator':ContentCreators.objects.all()})










