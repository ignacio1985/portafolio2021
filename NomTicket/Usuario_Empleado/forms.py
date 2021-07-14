from django import forms
from CORE.models import EMPLEADO,TICKET

class empleadoForm(forms.ModelForm):
    clave = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = EMPLEADO
        fields = '__all__'
        
class loginEmpForm(forms.ModelForm):
    clave=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = EMPLEADO
        fields = ['rut_emp', 'clave']
        
class guardarpedido(forms.ModelForm):
    class Meta:
        model = TICKET
        fields = '__all__'

class rec_con_Form(forms.ModelForm):
    rut_emp = forms.CharField(widget=forms.TextInput(attrs={'oninput' : "checkRut(this)"}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}))
    class Meta:
        model = EMPLEADO
        fields = ['rut_emp', 'email']
    
