from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from web.forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile

class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = ['username', 'fullname', 'address', 'birthdate', 'nic', 'mobilephone', 'homephone', 'email']

admin.site.register(Profile, ProfileAdmin)
