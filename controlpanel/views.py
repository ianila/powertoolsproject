from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm

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

        if user is not None and user.is_active and user.isstaff or user.isroot:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

class LogOutView(generic.RedirectView):
    url = reverse_lazy('cplogin')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)
