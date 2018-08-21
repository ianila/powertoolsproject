from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import Profile

class LoginForm(AuthenticationForm):

    class Meta():
        model = Profile
        fields = ('username', 'password')
