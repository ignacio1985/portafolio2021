from django import forms
from CORE.models import TICKET

class CrearTicket(forms.ModelForm):
    class Meta:
        model = TICKET
        fields = [
            'valor',
            'fk_codigo_emp',
            'fk_tipo_ticket',
        ]