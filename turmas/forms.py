from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Estudante, Professor, Turma, Matricula

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
        fields = ("email", "username", "password1", "password2")
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_estudante = True
        user.save()
        estudante = Estudante.objects.create(user=user)
        return user

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ('nome', 'professor')

class MatriculaForm(forms.ModelForm):
    estudantes = forms.ModelMultipleChoiceField(
        queryset=Estudante.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta:
        model = Matricula
        fields = ('estudantes', )