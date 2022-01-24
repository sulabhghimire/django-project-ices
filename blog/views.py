from django.shortcuts import render
from django.http import HttpResponse
from django.template import context #to give HTTP RESPONSES
from .models import Article

#Class based views sajilo hunxa, override 
#Function based views use

def homepage(request):

    articles    = Article.objects.all().order_by('-date_created')
    

    context     = {
        'posts'  : articles,
    }

    return render(request, 'blog/home.html', context)

# Create your views here.
# ALL YOUR LOGIC GOES HERE