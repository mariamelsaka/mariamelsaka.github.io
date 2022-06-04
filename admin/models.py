from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Podcasts(models.Model):
        podcast_id = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='podcast_id')
        title = models.TextField(max_length=100)
        content_creator_name=models.CharField(max_length=50)
        description = models.TextField(max_length=100)
        podcast_url=models.URLField(max_length=300)
        views = models.IntegerField()



class Videos(models.Model):
        video_id = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='video_id')
        title = models.TextField(max_length=100)
        description = models.TextField(max_length=100)
        video_url=models.URLField(max_length=300)
        content_creator_name=models.CharField(max_length=50)
        views = models.IntegerField()




class ContentCreators(models.Model):
    creators_id = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='creators_id')
    name=models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    
    video_content =models.ForeignKey(Videos,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name="video_coontent",
                                )
    
    podcast_content =models.ForeignKey(Podcasts,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name="podcast_content",
                                )



class customAdmins(models.Model):
    user = models.OneToOneField(User, related_name="admin_v2", null=True, on_delete=models.CASCADE)
    dateofbirth= models.DateField()
    GENDER_CHOICES=(
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES ,default=None)
    password= models.CharField(max_length=50)
    
    podcast =models.ForeignKey(Podcasts,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name="podcasts",
                                )
    content_creator =models.ForeignKey(ContentCreators,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name="contentcreators",
                                )
    video =models.ForeignKey(Videos,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name="videos",
                                )









