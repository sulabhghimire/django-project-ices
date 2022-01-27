from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

def profile(request, pk):
    
    data = User.objects.get(id = pk)

    context = {
        'user_data' : data,
    }

    return render(request, 'accounts/profile.html', context)
