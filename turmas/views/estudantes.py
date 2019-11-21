from django.views.generic import CreateView, ListView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib import messages

from ..models import User, Estudante, Turma, Atividade, Problema, Submissao
from ..forms import EstudanteSignUpForm, SubmissaoForm
from ..decorators import estudante_required

from radon.cli.tools import iter_filenames
from radon.raw import analyze
from radon.metrics import h_visit

class EstudanteSignUpView(CreateView):
    model = User
    form_class = EstudanteSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'estudante'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

@method_decorator([login_required, estudante_required], name='dispatch')
class TurmaListView(ListView):
    model = Turma
    ordering = ('nome', )
    context_object_name = 'turmas'
    template_name = 'usuario/estudantes/listar_turmas_estudante.html'
    paginate_by = 5

    def get_queryset(self):
        estudante = self.request.user.id
        queryset = Turma.objects.filter(estudantes__pk=estudante)
        return queryset

@login_required
@estudante_required
def listar_atividades(request, pk):
    atividades = Atividade.objects.filter(turma__pk=pk)
    return render(request, 'usuario/estudantes/listar_atividades_estudante.html', {'atividades': atividades})

@login_required
@estudante_required
def listar_problemas(request, pk):
    problemas = Problema.objects.filter(atividade__pk=pk)
    return render(request, 'usuario/estudantes/listar_problemas_estudante.html', {'problemas': problemas})

@login_required
@estudante_required
def adicionar_submissao(request, pk):
    estudante = request.user.estudante
    problema = get_object_or_404(Problema, pk=pk)

    if request.method == 'POST':
        form = SubmissaoForm(request.POST, request.FILES)
        if form.is_valid():
            submissao = form.save(commit=False)
            submissao.estudante = estudante
            submissao.problema = problema
            
            arquivo = request.FILES['codigo']
            codigo = arquivo.read().decode('utf-8')
            
            raw = analyze(codigo)
            hal = h_visit(codigo)
            
            submissao.raw_loc = raw.loc
            submissao.raw_lloc = raw.lloc
            submissao.raw_sloc = raw.sloc
            submissao.hal_total_h1 = hal.total.h1
            submissao.hal_total_h2 = hal.total.h2
            submissao.hal_total_N1 = hal.total.N1
            submissao.hal_total_N2 = hal.total.N2
            submissao.hal_total_vocabulary = hal.total.vocabulary
            submissao.hal_total_length = hal.total.length
            submissao.hal_total_calculated_length = hal.total.calculated_length
            submissao.hal_total_volume = hal.total.volume
            submissao.hal_total_difficulty = hal.total.difficulty
            submissao.hal_total_effort = hal.total.effort
            submissao.hal_total_time = hal.total.time
            submissao.hal_total_bugs = hal.total.bugs
            submissao.save()
            messages.success(request, 'Submissão realizada com sucesso!')
            return redirect('estudantes:adicionar_submissao', problema.pk)
    else:
        form = SubmissaoForm()
    return render(request, 'usuario/estudantes/adicionar_submissao_form.html', {'problema': problema, 'form': form})

@login_required
@estudante_required
def listar_submissoes(request, pk):
    submissoes = Submissao.objects.filter(problema__pk=pk)
    return render(request, 'usuario/estudantes/listar_submissoes_estudante.html', {'submissoes': submissoes})