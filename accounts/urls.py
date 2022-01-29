from django.urls import path, include #we imported include
from .views import profile, register_request, log_in, log_out, update_profile
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

urlpatterns = [
    path('profile/<int:pk>/', profile, name='profile'),
    path('register/', register_request, name='register'),
    path('login/', log_in, name="login"),
    path('log_out/', log_out, name="log_out"),
    path('profile_update/', update_profile, name="profile-update"),
    path('password_change/', 
        PasswordChangeView.as_view(
            template_name = 'accounts/password_change_form.html',
            success_url = reverse_lazy('login')
        ),
        name='password_change'),
]