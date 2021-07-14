from django import forms
from CORE.models import VISITANTE,TICKET
        
class visitanteForm(forms.ModelForm):
    class Meta:
        model = VISITANTE
        fields = ['rut_visitante']
        
class guardarpedido(forms.ModelForm):
    class Meta:
        model = TICKET
        fields = '__all__'
    
