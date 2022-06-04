from django.urls import path #django.urls libary to connect to urls
from . import views
from django.contrib.auth import views as auth_views #logout

urlpatterns = [
    path ("admin_login",views.admin_login,name="admin_login"),
    path ("add_video",views.add_video,name="add_video"),
    path ("add_content",views.add_content,name="add_content"),
    path ("add_video_content",views.create,name="add_video_content"),
    path ("add_content_creators",views.create_content_creators,name="add_content_creators"),
    path ("show_content_creators",views.show_content_creators,name="show_content_creators"),
    path ("error",views.error,name="error"),
    path("show_video",views.show_videos ,name="show_video"),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('<int:id>/update_video', views.update_video, name='update_video'), # PUT (UPDATE)
    path('<int:id>/delete_video', views.delete_video, name='delete_video'),  # Delete (DELETE)
    path('<int:id>', views.show_specific, name='show_specific') # GET  (READ)
]

