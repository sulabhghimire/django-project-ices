from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.db import transaction


from accounts.models import Profile
User    = get_user_model()

# Django comes with a pre-built register form called UserCreationForm that connects to 
# the pre-built model User. However, the UserCreationForm only requires a username and 
# password (password1 is the initial password and password2 is the password confirmation).

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model   = User
        fields  = ("email", "username", "first_name", "last_name", "date_o_b", "bio", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=True)
        return user

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model   = User
        fields  = ("first_name", "last_name", "date_o_b", "bio",)

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model   = Profile
        fields  = ("pic",)

class UserDeleteForm(forms.ModelForm):

    class Meta:
        model   = User
        fields = []