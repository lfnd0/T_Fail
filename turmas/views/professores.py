from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.db.models import Count

from ..models import User, Turma
from ..forms import ProfessorSignUpForm
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
        return redirect('professores:listar_turmas')

@method_decorator([login_required, professor_required], name='dispatch')
class TurmaListView(ListView):
    model = Turma
    ordering = ('nome', )
    context_object_name = 'turmas'
    template_name = 'usuario/professores/listar_turmas.html'

    def get_queryset(self):
        queryset = self.request.user.professor.turmas
        return queryset

@method_decorator([login_required, professor_required], name='dispatch')
class TurmaCreateView(CreateView):
    model = Turma
    fields = ('nome', )
    template_name = 'usuario/professores/adicionar_turma_form.html'

    def form_valid(self, form):
        turma = form.save(commit=False)
        turma.professor = self.request.user.professor
        turma.save()
        return redirect('professores:listar_turmas')

@method_decorator([login_required, professor_required], name='dispatch')
class TurmaUpdateView(UpdateView):
    model = Turma
    fields = ('estudantes', )
    context_object_name = 'turma'
    template_name = 'usuario/professores/atualizar_turma_form.html'
    
    def get_queryset(self):
        return self.request.user.professor.turmas.all()
    
    def get_success_url(self):
        return reverse('professores:listar_turmas')