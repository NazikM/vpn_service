from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as auth_views

from user_management.views import RegistrationView, LoginView, UpdateProfileView

app_name = "profile"

urlpatterns = [
    path('<int:pk>', login_required(UpdateProfileView.as_view()), name='profile'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout")
]
