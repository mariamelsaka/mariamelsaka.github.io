from django.urls import path #django.urls libary to connect to urls
from . import views

urlpatterns = [
    path ("da7e7",views.da7e7,name="da7e7"),
    path ("egychology",views.egychology,name="egychology"),
    path ("eman",views.eman,name="eman"),
    path ("home",views.home,name="home"),
    path ("profile",views.profile,name="profile"),
    path ("login",views.login,name="login"),
    path ("register",views.register,name="register"),
    path ("accounts_setting",views.accounts_setting,name="accounts_setting"),
]


