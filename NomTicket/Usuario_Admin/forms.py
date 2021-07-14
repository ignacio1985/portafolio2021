from django import forms
from CORE.models import EMPLEADO

class empleadoForm(forms.ModelForm):
    #clave = forms.CharField(widget=forms.PasswordInput(attrs={'onclick':'muestraContraseña()','placeholder': 'Minimo 8 caracteres'},render_value=True))
    #clave = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Minimo 8 caracteres'},render_value=True),max_length=10,min_length=8)
    clave = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'ingrese contraseña'},render_value=True))
    rut_emp = forms.CharField(widget=forms.TextInput(attrs={'oninput' : "checkRut(this)"}))
    #rut_emp = forms.CharField(widget=forms.TextInput(attrs={'oninput' : "checkRut(this)",'placeholder': 'Ingrese rut sin puntos'}),max_length=10)
    email = forms.EmailField(widget = forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}))
    nom_emp =forms.CharField(widget = forms.TextInput(attrs={'onkeypress': 'return SoloLetras(event)','placeholder': 'texto ´','onpaste':'return false'}))
    appaterno_emp =forms.CharField(widget = forms.TextInput(attrs={'onkeypress': 'return SoloLetras(event)','placeholder': 'texto ´','onpaste':'return false'}))
    apmaterno_emp =forms.CharField(widget = forms.TextInput(attrs={'onkeypress': 'return SoloLetras(event)','placeholder': 'texto ´','onpaste':'return false'}))
    class Meta:
        model = EMPLEADO
        fields = '__all__'
        
class loginEmpForm(forms.ModelForm):
    clave=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = EMPLEADO
        fields = ['rut_emp', 'clave']


    
