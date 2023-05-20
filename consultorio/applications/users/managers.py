from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, password, is_staff, is_superuser, is_active, **extra_fields):
        extra_fields.setdefault('ocupation', '0')  # Asignar ocupation como "administrator"
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, True, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        return self._create_user(username, password, True, True, True, **extra_fields)
    

    def usuarios_administradores(self):
        return self.filter(
            ocupation='0'
        ).order_by('-last_login')
        
    def usuarios_asistentes(self):
        return self.filter(
            ocupation='1'
        ).order_by('-last_login')
                
        
class PatientManager(BaseUserManager, models.Manager):

    def _create_user(self, username, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, True, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        return self._create_user(username, password, True, True, True, **extra_fields)
    
    def usuarios_pacientes(self):
        return self.filter(
            is_active=True
        ).order_by('last_name')