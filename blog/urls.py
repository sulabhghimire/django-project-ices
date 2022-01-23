from django.urls import path
from .views import homepage #importing our homepage function

urlpatterns = [
    path('', homepage, name="home"),
]