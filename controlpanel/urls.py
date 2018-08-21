from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='cphome'),
    path('login/', views.LoginView.as_view(), name='cplogin'),
    path('logout/', views.LogOutView.as_view(), name='cplogout'),
    path('staff/', views.cpstaff, name='cpstaff'),
    path('newstaff/', views.staff_create, name='cpnewstaff'),
]
