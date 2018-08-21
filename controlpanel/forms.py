from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import Profile

class LoginForm(AuthenticationForm):

    class Meta():
        model = Profile
        fields = ('username', 'password')

class StaffCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('username', 'fullname', 'address', 'birthdate', 'nic', 'mobilephone', 'homephone', 'email', 'isstaff', 'iscustomer')

