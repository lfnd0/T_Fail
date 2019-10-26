from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib import messages

from ..models import User, Turma, Atividade, Problema
from ..forms import ProfessorSignUpForm, AtividadeForm, ProblemaForm
from ..decorators import professor_required

class ProfessorSignUpView(CreateView):
    model = User
    form_class = ProfessorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'professor'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('professores:listar_turmas_professor')

@method_decorator([login_required, professor_required], name='dispatch')
class TurmaListView(ListView):
    model = Turma
    ordering = ('nome', )
    context_object_name = 'turmas'
    template_name = 'usuario/professores/listar_turmas_professor.html'
    paginate_by = 5

    def get_queryset(self):
        professor = self.request.user.id
        queryset = Turma.objects.filter(professor__pk=professor)
        return queryset

@method_decorator([login_required, professor_required], name='dispatch')
class TurmaCreateView(CreateView):
    model = Turma
    fields = ('nome', 'instituto', )
    template_name = 'usuario/professores/adicionar_turma_form.html'

    def form_valid(self, form):
        turma = form.save(commit=False)
        turma.professor = self.request.user.professor
        turma.save()
        messages.success(self.request, 'Sua turma foi adicionada com sucesso!')
        return redirect('professores:listar_turmas_professor')

@method_decorator([login_required, professor_required], name='dispatch')
class TurmaUpdateView(UpdateView):
    model = Turma
    fields = ('estudantes', )
    context_object_name = 'turma'
    template_name = 'usuario/professores/atualizar_turma_form.html'
    
    def get_queryset(self):
        return self.request.user.professor.turmas.all()
    
    def get_success_url(self):
        return reverse('professores:listar_turmas_professor')

@login_required
@professor_required
def deletar_turma(request, id):
    turma = get_object_or_404(Turma, pk=id)
    turma.delete()
    messages.info(request, 'Turma deletada com sucesso!')
    return redirect('professores:listar_turmas_professor')

@login_required
@professor_required
def listar_atividades(request, pk):
    atividades = Atividade.objects.filter(turma__pk=pk)
    return render(request, 'usuario/professores/listar_atividades_professor.html', {'atividades': atividades})

@login_required
@professor_required
def adicionar_atividade(request, pk):
    turma = get_object_or_404(Turma, pk=pk, professor=request.user.professor)

    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            atividade = form.save(commit=False)
            atividade.turma = turma
            atividade.save()
            messages.success(request, 'Sua atividade foi adicionada com sucesso!')
            return redirect('professores:listar_atividades_professor', turma.pk)
    else:
        form = AtividadeForm()
    return render(request, 'usuario/professores/adicionar_atividade_form.html', {'turma': turma, 'form': form})


@login_required
@professor_required
def listar_problemas(request, pk):
    problemas = Problema.objects.filter(atividade__pk=pk)
    return render(request, 'usuario/professores/listar_problemas_professor.html', {'problemas': problemas})

@login_required
@professor_required
def adicionar_problema(request, pk):
    atividade = get_object_or_404(Atividade, pk=pk)

    if request.method == 'POST':
        form = ProblemaForm(request.POST)
        if form.is_valid():
            problema = form.save(commit=False)
            problema.atividade = atividade
            problema.save()
            messages.success(request, 'Seu problema foi adicionado com sucesso!')
            return redirect('professores:listar_problemas_professor', atividade.pk)
    else:
        form = ProblemaForm()
    return render(request, 'usuario/professores/adicionar_problema_form.html', {'atividade': atividade, 'form': form})
