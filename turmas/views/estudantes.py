from django.views.generic import CreateView, ListView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage


from ..models import User, Estudante, Turma, Submissao
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

@method_decorator([login_required, estudante_required], name='dispatch')
class SubmissaoCreateView(CreateView):
    model = Submissao
    form_class = SubmissaoForm
    template_name = 'usuario/estudantes/adicionar_submissao_form.html'

    def form_valid(self, form):
        submissao = form.save(commit=False)   
        submissao.estudante = self.request.user.estudante
        arquivo = self.request.FILES['codigo']
        
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
        return redirect('estudantes:listar_turmas_estudante')