from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='cphome'),
    path('login/', views.LoginView.as_view(), name='cplogin'),
    path('logout/', views.LogOutView.as_view(), name='cplogout'),
    path('staff/', views.cpstaff, name='cpstaff'),
    path('newstaff/', views.staff_create, name='cpnewstaff'),
    path('editstaff/', views.staff_edit, name='cpeditstaff'),
    path('updatestaff/', views.staff_update, name='cpupdatestaff'),
    path('deletestaff/', views.staff_delete, name='cpdeletestaff'),
]
