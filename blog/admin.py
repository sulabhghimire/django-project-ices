from django.contrib import admin
from .models import Article #importing the Article model from models.py

admin.site.register(Article) #registering the article model


# Register your models here to be shown in django admin.
