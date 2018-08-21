from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Profile

class ProfileCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('username', 'fullname', 'address', 'birthdate', 'nic', 'mobilephone', 'homephone', 'email')

class ProfileLoginForm(AuthenticationForm):

    class Meta():
        model = Profile
        fields = ('username', 'password')

class ProfileChangeForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = ('username', 'fullname', 'address', 'birthdate', 'nic', 'mobilephone', 'homephone', 'email')

