from django.shortcuts import redirect, render
from ..models import Turma

from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count

from ..decorators import professor_required

@method_decorator([login_required, professor_required], name='dispatch')
class TurmaListView(ListView):
    model = Turma
    ordering = ('nome', )
    context_object_name = 'turmas'
    template_name = 'professor/professor_home.html'

    def get_queryset(self):
        queryset = self.request.user.professor.turmas
        return queryset

@method_decorator([login_required, professor_required], name='dispatch')
class TurmaCreateView(CreateView):
    model = Turma
    fields = ('nome', )
    template_name = 'professor/adicionar_turma.html'

    def form_valid(self, form):
        turma = form.save(commit=False)
        turma.professor = self.request.user.professor
        turma.save()
        return redirect('professor_home')