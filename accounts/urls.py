from django.urls import path, include #we imported include
from .views import profile, register_request, log_in, log_out, update_profile, delete_user
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

urlpatterns = [
    path('profile/<int:pk>/', profile, name='profile'),
    path('register/', register_request, name='register'),
    path('login/', log_in, name="login"),
    path('log_out/', log_out, name="log_out"),
    path('profile_update/', update_profile, name="profile-update"),
    path('delete_account/', delete_user, name="delete_account"),
    path('password_change/', 
        PasswordChangeView.as_view(
            template_name = 'accounts/password_change_form.html',
            success_url = reverse_lazy('login')
        ),
        name='password_change'),
    path('password_reset/', 
        PasswordResetView.as_view(
            template_name = 'accounts/password_reset_form.html',
        ),
        name='password_reset'),
    path('password_reset/done', 
        PasswordResetDoneView.as_view(
            template_name = 'accounts/password_reset_done.html',
        ),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name = 'accounts/password_reset_confirm.html'
        ),
        name="password_reset_confirm"),
    path('reset/done/',
        PasswordResetCompleteView.as_view(
            template_name = 'accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'),
]