from django.shortcuts import render
from django.http import HttpResponse #to give HTTP RESPONSES

#Class based views sajilo hunxa, override 
#Function based views use

def homepage(request):
    
    return HttpResponse(""" 
        <h1> Hello </h1>
    """)

# Create your views here.
# ALL YOUR LOGIC GOES HERE