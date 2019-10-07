from django.views.generic import CreateView, ListView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage


from ..models import User, Estudante, Turma, Submissao
from ..forms import EstudanteSignUpForm, SubmissaoForm
from ..decorators import estudante_required

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

class SubmissaoCreateView(CreateView):
    model = Submissao
    form_class = SubmissaoForm
    template_name = 'usuario/estudantes/adicionar_submissao_form.html'

    def form_valid(self, form):
        resposta = form.save(commit=False)
        resposta.estudante = self.request.user.estudante
        resposta.save()
        return redirect('estudantes:listar_turmas_estudante')