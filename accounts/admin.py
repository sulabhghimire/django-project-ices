from django.contrib import admin
from .models import CustomUser, Profile


admin.site.register(Profile)
admin.site.register(CustomUser)


# Register your models here.
