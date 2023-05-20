from django import forms
from django.contrib.auth import authenticate
#
from .models import User, Patient

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'input-group-field',
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'class': 'input-group-field',
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'username',
            'name',
            'last_name',
            'ocupation',
            'gender',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre de Usuario ...',
                    'class': 'input-group-field',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres ...',
                    'class': 'input-group-field',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Apellidos ...',
                    'class': 'input-group-field',
                }
            ),
            'ocupation': forms.Select(
                attrs={
                    'placeholder': 'Ocupacion ...',
                    'class': 'input-group-field',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'placeholder': 'Genero ...',
                    'class': 'input-group-field',
            }
            ),
           
        }
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-group-field',
                'placeholder': 'Nombre Usuario',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-group-field',
                'placeholder': 'contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data


class UserUpdateForm(forms.ModelForm):

    class Meta:

        model = User
        fields = (
            'username',
            'name',
            'last_name',
            'ocupation',
            'gender',
            'is_active',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre de Usuario ...',
                    'class': 'input-group-field',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres ...',
                    'class': 'input-group-field',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Apellidos ...',
                    'class': 'input-group-field',
                }
            ),
            'ocupation': forms.Select(
                attrs={
                    'placeholder': 'Ocupacion ...',
                    'class': 'input-group-field',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'placeholder': 'Genero ...',
                    'class': 'input-group-field',
                }
            ),
            
            'is_active': forms.CheckboxInput(
                attrs={
                },
            ),
        }


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )
    
    
    
    
    
    
    
class PatientRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'input-group-field',
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'class': 'input-group-field',
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = Patient
        fields = (
            'username',
            'name',
            'last_name',
            'gender',
            'date_birth',
            'altura',
            'peso',
            'actividad_aerobica',
            
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre de Usuario ...',
                    'class': 'input-group-field',
                }
            ),
            
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres ...',
                    'class': 'input-group-field',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Apellidos ...',
                    'class': 'input-group-field',
                }
            ),
            
            'gender': forms.Select(
                attrs={
                    'placeholder': 'Genero ...',
                    'class': 'input-group-field',
            }
            ),
            
            'date_birth': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
            
            'altura': forms.NumberInput(
                attrs = {
                    'placeholder': '1',
                    'class': 'input-group-field',
                }
            ),
            
           'peso': forms.NumberInput(
                attrs = {
                    'placeholder': '1',
                    'class': 'input-group-field',
                }
            ),
            
            
        
           'actividad_aerobica': forms.CheckboxInput(),
           
        }
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')
            
            
            
            
class PatientUpdateForm(forms.ModelForm):

    class Meta:

        model = Patient
        fields = (
            'username',
            'name',
            'last_name',
            'gender',
            'date_birth',
            'peso',
            'altura',
            'actividad_aerobica',
            'is_active',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre de Usuario ...',
                    'class': 'input-group-field',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres ...',
                    'class': 'input-group-field',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Apellidos ...',
                    'class': 'input-group-field',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'placeholder': 'Genero ...',
                    'class': 'input-group-field',
                }
            ),
            
            'date_birth': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
            
            
            'peso': forms.NumberInput(
                attrs = {
                    'placeholder': '1',
                    'class': 'input-group-field',
                }
            ),
            
            'altura': forms.NumberInput(
                attrs = {
                    'placeholder': '1',
                    'class': 'input-group-field',
                }
            ),
            
            'actividad_aerobica': forms.CheckboxInput(),
            
            'is_active': forms.CheckboxInput(
                attrs={
                },
            ),
        }
