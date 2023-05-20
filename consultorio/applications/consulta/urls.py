#
from django.urls import path

from . import views

app_name = "consulta_app"

urlpatterns = [
    

    path(
        'consulta/historial/<pk>/', 
        views.HistorialConsultas.as_view(),
        name='historial-consulta-paciente',
    ),
    
    path(
        'consulta/add/<pk>/', 
        views.ConsultaCreateView.as_view(),
        name='add-consulta-paciente',
    ),
        
   
]