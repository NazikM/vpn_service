from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView

from user_management.forms import RegistrationForm, UserProfileForm
from user_management.models import UserProfile


class RegistrationView(FormView):
    template_name = 'user_management/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('vpn:list')

    def form_valid(self, form):
        user = form.save()
        UserProfile(user=user).save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'user_management/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('vpn:list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class UpdateProfileView(UpdateView):
    template_name = 'user_management/profile.html'
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('vpn:list')


