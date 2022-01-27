from django.urls import path, include #we imported include
from .views import profile

urlpatterns = [
    path('profile/<int:pk>/', profile, name='profile'),
]