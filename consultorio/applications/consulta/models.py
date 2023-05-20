from django.db import models
from applications.users.models import Patient, User
from django.conf import settings
# Create your models here.
from .managers import ConsultaManager

class Consulta(models.Model):
    patient = models.ForeignKey(Patient, related_name='assignedleads', blank=True, null=True, on_delete=models.SET_NULL)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    observations = models.TextField(
        'Observaciones',
        blank=False,
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    objects = ConsultaManager()