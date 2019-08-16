from django.shortcuts import redirect, render
from .models import Turma
from .forms import TurmaForm

def listar_turmas(request):
    data = {}
    data['turmas'] = Turma.objects.all()
    return render(request, 'professor/listagem_turmas.html', data)

def criar_nova_turma(request):
    data = {}
    form = TurmaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listagem_turmas')

    data['form'] = form
    return render(request,'professor/form.html', data)