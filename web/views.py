from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout

from .forms import ProfileCreationForm, ProfileLoginForm

class SignUp(generic.CreateView):
    form_class = ProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'web/signup.html'

class LoginView(generic.FormView):
    form_class = ProfileLoginForm
    success_url = reverse_lazy('home')
    template_name = 'web/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active and user.iscustomer:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

class LogOutView(generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)
