#
from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        '', 
        views.LoginUser.as_view(),
        name='user-login',
    ),
    
    path(
        'home/', 
        views.Home.as_view(),
        name='home',
    ),
    
    path(
        'users/logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    
    path(
        'users/register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'users/update-password/<pk>/', 
        views.UpdatePasswordView.as_view(),
        name='user-update_password',
    ),
    path(
        'users/update/<pk>/', 
        views.UserUpdateView.as_view(),
        name='user-update',
    ),
    path(
        'users/delete/<pk>/', 
        views.UserDeleteView.as_view(),
        name='user-delete',
    ),
    path(
        'users/lista/', 
        views.UserListView.as_view(),
        name='user-lista',
    ),
    path(
        'users/lista/asistentes', 
        views.AssistantListView.as_view(),
        name='user-lista-assistant',
    ),
    path(
        'users/lista/pacientes', 
        views.PatientListView.as_view(),
        name='user-lista-patient',
    ),
    
    path(
        'users/registra/pacientes', 
        views.PatientRegisterView.as_view(),
        name='user-register-patient',
    ),
    
    path('patient-detail/<pk>/',views.PatientDetailView.as_view(),
        name='patient_detail'
    ),
    
    path(
        'users/update/paciente/<pk>/', 
        views.PatientUpdateView.as_view(),
        name='user-update-paciente',
    ),
    
    path(
        'users/lista/pacientes/asistente', 
        views.PatientListViewAssistant.as_view(),
        name='user-lista-patient-assistant',
    ),
        
    path(
        'users/update/paciente/assistant/<pk>/', 
        views.PatientDetailViewAssistant.as_view(),
        name='user-update-paciente-assistant',
    ),
    
    
    path('status/',views.PatientStatus.as_view(),
        name='status-patient'
        
    ),
   
]