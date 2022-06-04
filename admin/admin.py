from django.contrib import admin
from .models import customAdmins,Videos,Podcasts , ContentCreators



admin.site.register(Podcasts)
admin.site.register(customAdmins)
admin.site.register(Videos)
admin.site.register(ContentCreators)
# Register your models here.
