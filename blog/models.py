from operator import mod
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# you will create database classes here
# TYPES OF RELATIONSHIP 
#   1. One to One  OnetoOneFIeld
    # 2. one to may ForeginKey
    # 3. many to many   ManyToManyField

class Article(models.Model):
    
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=30, null=False, blank=False)
    content     = models.TextField(null=False, blank=False)
    date_created= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.author}.'

    