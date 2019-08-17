from django.forms import ModelForm
from .models import Turma

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'professor']