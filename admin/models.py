from django.db import models
from datetime import datetime
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
        content_creator_name=models.CharField(max_length=50)
        description = models.TextField(max_length=100)
        video_url=models.URLField(max_length=300)
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
    
    
class Admins(models.Model):
    admin_id = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='admin_id')
    fisrt_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    phone_number = models.TextField(max_length=11 , default='')
    address = models.TextField(max_length=60)
    email = models.EmailField(max_length=60)
    username = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime)
    updated_at = models.DateTimeField(default=datetime)
    dateofbirth= models.DateTimeField(auto_now=True)
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


class SuperAdmins(models.Model):
    superadmin_id = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='superadmin_id')
    fisrt_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    phone_number = models.TextField(max_length=11 , default='')
    address = models.TextField(max_length=60)
    email = models.EmailField(max_length=60)
    username = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime)
    updated_at = models.DateTimeField(default=datetime)
    dateofbirth= models.DateField()
    GENDER_CHOICES=(
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES ,default=None)
    password= models.CharField(max_length=50)
    admin =models.ForeignKey(Admins,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name="admins",
                                )



