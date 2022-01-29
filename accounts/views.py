from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
User = get_user_model()
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def profile(request, pk):
    
    data = User.objects.get(id = pk)

    context = {
        'user_data' : data,
    }

    return render(request, 'accounts/profile.html', context)

def register_request(request):

    if not request.user.is_authenticated:
        if request.method == "POST":
            form    = UserRegistrationForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                print(data)
                form.save()
                messages.success(request, "Registration is Sucessfull.")
                return redirect("home")
            messages.error(request, "Unsucessful registration. Invlid information.")
        
        form    = UserRegistrationForm()
        context = {
            'form'  : form
        }
        return render(request, "accounts/register.html", context)
    else:
        return redirect(reverse('home'))

def log_in(request):

    if not request.user.is_authenticated:
        if request.method == "POST":
            form    = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                print(form)
                print(form.cleaned_data)
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You have logged in as {username}.")
                    return redirect("home")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")

        form    = AuthenticationForm()
        context = {
            'form'  : form
        }
        return render(request, "accounts/login.html", context)
    
    else:
        return redirect("home")

@login_required
def log_out(request):

    logout(request)
    messages.success(request, "You have sucessfully logged out.")
    return redirect(reverse("home"))

@login_required
def update_profile(request):
    
    if request.method == "POST":
        u_a         = UserUpdateForm(request.POST, instance=request.user)
        u_p         = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_p.is_valid() and u_a.is_valid():
            u_a.save()
            u_p.save()
            messages.success(request, "Your Profile has been updated!")
            return redirect(reverse('profile', kwargs={'pk': request.user.pk}))
        else:
            messages.warning(request, "Invalid Form")

    u_a  = UserUpdateForm(instance=request.user)
    u_p  = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_a' : u_a,
        'u_p' : u_p,
    }

    return render(request, "accounts/update_profile.html", context)