from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Estudante, Professor, Turma, Submissao, Atividade, Problema, Avaliacao

class ProfessorSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Obrigatório. 60 caracteres ou menos.')
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit= True):
        user = super().save(commit=False)
        user.is_professor = True
        user.save()
        professor = Professor.objects.create(user=user)
        return user

class EstudanteSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Obrigatório. 60 caracteres ou menos.')
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_estudante = True
        user.save()
        estudante = Estudante.objects.create(user=user)
        return user

class SubmissaoForm(forms.ModelForm):
    codigo = forms.FileField(label='')
    class Meta:
        model = Submissao
        fields = ('codigo', )

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ('titulo', )

class ProblemaForm(forms.ModelForm):
    class Meta:
        model = Problema
        fields = ('pergunta', )

class AvaliacaoForm(forms.ModelForm):
    nota = forms.FloatField(min_value=0.0, max_value=10.0)
    class Meta:
        model = Avaliacao
        fields = ('nota', 'observacao', )