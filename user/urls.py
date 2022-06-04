from turtle import up
from django.urls import path #django.urls libary to connect to urls
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ("home",views.home,name="home"),
    path ("login",views.login,name="login"),
    path ("register",views.register,name="register"),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path("egychology",views.show_eg_content ,name="egychology"),
    path("da7e7",views.show_d7e7_content ,name="da7e7"),
    path("eman",views.show_eman_content ,name="eman")
    
]
    


