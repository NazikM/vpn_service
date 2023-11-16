from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from user_management.models import UserProfile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password2']:
            self.fields[fieldname].help_text = None


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


class ChangePasswordForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['password']
