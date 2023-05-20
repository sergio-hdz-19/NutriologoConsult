from django.contrib.auth.models import BaseUserManager
from django.db import models


class ConsultaManager(BaseUserManager, models.Manager):

    
    
    def historial_consulta_paciente(self, pk):
        return self.filter(
            patient=pk
        ).order_by('-created_at')
        
        
    def historial_consulta_by_id(self, pk):
        return self.filter(
            patient__id=pk
        ).order_by('created_at')
        
    