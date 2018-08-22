from django import forms
from django.forms import ModelForm, TextInput, EmailInput, CheckboxInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from users.models import Profile

class LoginForm(AuthenticationForm):

    class Meta():
        model = Profile
        fields = ('username', 'password')

class StaffCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('username', 'fullname', 'address', 'birthdate', 'nic', 'mobilephone', 'homephone', 'email', 'isstaff', 'iscustomer')

class StaffEditForm(ModelForm):

    class Meta():
        model = Profile
        fields = ('username', 'fullname', 'address', 'birthdate', 'nic', 'mobilephone', 'homephone', 'email')

        widgets = {
            'username': TextInput(attrs={'class': 'w3-input w3-border', 'autofocus': 'True', 'id': 'username', 'required': True}),
            'fullname': TextInput(attrs={'class': 'w3-input w3-border', 'id': 'fullname', 'required': True}),
            'address': TextInput(attrs={'class': 'w3-input w3-border', 'id': 'address', 'required': True}),
            'birthdate': TextInput(attrs={'class': 'w3-input w3-border', 'id': 'birthdate', 'required': True}),
            'nic': TextInput(attrs={'class': 'w3-input w3-border', 'id': 'nic', 'required': True}),
            'mobilephone': TextInput(attrs={'class': 'w3-input w3-border', 'id': 'mobilephone', 'required': True}),
            'homephone': TextInput(attrs={'class': 'w3-input w3-border', 'id': 'homephone', 'required': True}),
            'email': EmailInput(attrs={'class': 'w3-input w3-border', 'id': 'email', 'required': True}),
        }

