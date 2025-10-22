from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['instrumento', 'descripcion', 'fecha_pago', 'valor_historico']
        fields += [f'factor{i}' for i in range(8, 39)]
