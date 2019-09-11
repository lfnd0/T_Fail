from django.views.generic import CreateView, ListView
from django.contrib.auth import login
from django.shortcuts import redirect

from ..models import User, Estudante, Turma
from ..forms import EstudanteSignUpForm

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
    
class TurmaListView(ListView):
    model = Turma
    ordering = ('nome', )
    context_object_name = 'turmas'
    template_name = 'usuario/estudantes/listar_turmas_estudante.html'

    def get_queryset(self):
        estudante = self.request.user.username
        queryset = Turma.objects.filter(estudantes__in=estudante)
        return queryset
