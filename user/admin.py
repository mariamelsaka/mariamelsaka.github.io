from django.contrib import admin
from django.contrib.auth.models import User
from .models import customUsers

# Register your models here.
admin.site.register(customUsers)
