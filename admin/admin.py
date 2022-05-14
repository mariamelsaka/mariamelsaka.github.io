from django.contrib import admin
from .models import Admins ,SuperAdmins,Videos,Podcasts , ContentCreators

admin.site.register(Admins)
admin.site.register(SuperAdmins)
admin.site.register(Podcasts)
admin.site.register(Videos)
admin.site.register(ContentCreators)
# Register your models here.
