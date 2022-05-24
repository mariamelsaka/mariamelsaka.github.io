from django.urls import path #django.urls libary to connect to urls
from . import views

urlpatterns = [
    path ("admin_login",views.admin_login,name="admin_login"),
    path ("add_podcast",views.add_podcast,name="add_podcast"),
    path ("add_admin",views.add_admin,name="add_admin"),
    path ("add_video",views.add_video,name="add_video"),
    path ("add_content",views.add_content,name="add_content"),
    path ("admin_profile",views.admin_profile,name="admin_profile"),
    path ("dashboard",views.dashboard,name="dashboard"),
    path ("edit_content",views.edit_content,name="edit_content"),
    path ("edit_content2",views.edit_content2,name="edit_content2"),
    path ("edit_post",views.edit_post,name="edit_post"),
    path ("edit_post1",views.edit_post2,name="edit_post1"),

]


