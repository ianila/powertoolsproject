from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from users.models import Profile
from .forms import LoginForm, StaffCreationForm, StaffEditForm

class HomeView(generic.TemplateView):
    template_name = 'controlpanel/home.html'

class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('cphome')
    template_name = 'controlpanel/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active and not user.iscustomer:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

class LogOutView(generic.RedirectView):
    url = reverse_lazy('cplogin')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)

def cpstaff(request):
    users = Profile.objects.filter(isstaff=True)
    newform = StaffCreationForm()
    editform = StaffEditForm()
    return render(request, 'controlpanel/staff.html', {'users': users, 'newform': newform, 'editform': editform})

def staff_edit(request):
    profile = Profile.objects.get(pk=request.GET.get('pk'))
    data = { 'pk':profile.pk, 'username':profile.username, 'fullname':profile.fullname, 'address':profile.address, 'birthdate':profile.birthdate, 'nic':profile.nic, 'mobilephone':profile.mobilephone, 'homephone':profile.homephone, 'email':profile.email}
    return JsonResponse(data, safe=False)

def staff_create(request):
    form = StaffCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cpstaff')

def staff_update(request):
    print(request.POST.get('pk'))
    profile = Profile.objects.get(pk=request.POST.get('pk'))
    profile.username = request.POST.get('username')
    profile.fullname = request.POST.get('fullname')
    profile.address = request.POST.get('address')
    profile.birthdate = request.POST.get('birthdate')
    profile.nic = request.POST.get('nic')
    profile.mobilephone = request.POST.get('mobilephone')
    profile.homephone = request.POST.get('homephone')
    profile.email = request.POST.get('email')
    profile.save()
    
    return redirect('cpstaff')

def staff_delete(request):
    print(request.POST.get('pk'))
    Profile.objects.get(pk=request.POST.get('pk')).delete()       
    return redirect('cpstaff')


