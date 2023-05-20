from django import forms 

from .models import Consulta

class ConsultaForm(forms.ModelForm):
    
    class Meta:

        model = Consulta
        fields = (''
            'patient',
            'peso',
            'observations',
            
        )
        widgets ={
            
            
            
            'patient': forms.Select(
                attrs={
                    'placeholder': 'Ocupacion ...',
                    'class': 'input-group-field',
                }
            ),
            
            'peso': forms.NumberInput(
                attrs = {
                    'placeholder': '1',
                    'class': 'input-group-field',
                }
            ),
            
            'observations':forms.Textarea(),
        }




