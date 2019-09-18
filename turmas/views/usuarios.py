from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    return render(request, 'usuario/home.html')

def turma(request):
    if request.user.is_authenticated:
        if request.user.is_professor:
            return redirect('professores:listar_turmas_professor')
        else:
            return redirect('estudantes:listar_turmas_estudante')
    return render(request, 'usuario/home.html')