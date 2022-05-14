from django.db import models
from datetime import datetime #3ashan ytl3 time f l7zah el 7alyha

class Users(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='user_id')
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
    profile_pic = models.ImageField(default="static/img/profile_pic.jpg", null=True, blank=True)
# Create your models here.
