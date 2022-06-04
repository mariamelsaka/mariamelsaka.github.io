from django.shortcuts import render
from django.shortcuts import redirect,render
from .models import customUsers
from django.contrib.auth.models import User,auth
from admin.models import Videos
from django.contrib import messages

# Create your views here.



def home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "auth/login.html")

def register(request):
    return render(request, "auth/sign-up.html")



def register(request):
    if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            dateofbirth=request.POST['dateofbirth']
            psw = request.POST['psw']
            psw_repeat = request.POST['psw_repeat']
            phone_number=request.POST['phone_number']
            gender=request.POST['gender']
            if psw== psw_repeat: # بنشوف الباس صح ولا لأ مع عادته
              if User.objects.filter(username=username).exists():# لو عايز تدور على اي حاجة في الداتا بيز
               messages.info(request,'username is already exist')
               return redirect('register')
              elif User.objects.filter(email=email).exists():
               messages.info(request,'email is aleardy exist')
               return redirect('register')
              else:
               user = User.objects.create_user( first_name=first_name,last_name=last_name ,email=email,
               username=username,password=psw)  # عشان نعمل يوزر في الداتا بيز
               user.save()  # بيعمل حفظ للداتا في الداتا بيز
               custom_user = customUsers(user=user,dateofbirth=dateofbirth,phone_number=phone_number,gender=gender)
               custom_user.save()
               
               
               messages.info(request, 'user created')
               return redirect('home')
            else:
             messages.info(request,'password not matching..')
             return redirect('register')# بيرجع للصفحة الي قبليها علطول
    else:
            return render(request, 'auth/sign-up.html')
        
        
        
def login(request):
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    else:
         return render(request,'auth/login.html')
     


def show_eg_content(request):
    return render(request, "creators/ahmed samer.html",{'video':Videos.objects.filter( content_creator_name__contains="ahmed samir"   )})

def show_eman_content(request):
    return render(request, "creators/eman.html",{'video':Videos.objects.filter(content_creator_name__contains="eman elemam")})

def show_d7e7_content(request):
    return render(request, "creators/ahmed el3'andor.html",{'video':Videos.objects.filter(content_creator_name__contains="ahmed elghandor")})
