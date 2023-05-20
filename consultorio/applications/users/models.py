from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager, PatientManager

class User(AbstractBaseUser, PermissionsMixin):
    # TIPO DE USUARIOS
    ADMINISTRATOR = '0'
    ASSISTANT = '1'
    PATIENT = '2'
    # GENEROS
    MALE = 'M'
    WOMEN = 'F'
    OTHER = 'O'
    #
    OCUPATION_CHOICES = [
        (ADMINISTRATOR, 'Administrador'),
        (ASSISTANT, 'Asistente'),
        (PATIENT, 'Paciente'),
    ]

    GENDER_CHOICES = [
        (MALE, 'Masculino'),
        (WOMEN, 'Femenino'),
        (OTHER, 'Otros'),
    ]

    username = models.CharField('Usuario',max_length=100,unique=True)
    
    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellidos', max_length=100)
    
    ocupation = models.CharField(
        max_length=1, 
        choices=OCUPATION_CHOICES, 
        blank=True
    )
    
    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )
    
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField('Última conexión', blank=True, null=True)


    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.name + '  ' + self.last_name
    
    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()
    
    

class Patient(User):
    
    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    actividad_aerobica = models.BooleanField()
    
    objects = PatientManager()
    
    
    
    # def update_last_login(self):
    #     self.last_login = timezone.now()
    #     self.save()
    
   
