from django.shortcuts import redirect, render
from .models import Turma

from django.views.generic import CreateView, ListView


class TurmaListView(ListView):
    model = Turma
    ordering = ('name', )
    context_object_name = 'turmas'
    template_name = 'professor/professor_home.html'

    def get_queryset(self):
        queryset = self.request.user.turmas
        return queryset

class TurmaCreateView(CreateView):
    model = Turma
    fields = ('nome', )
    template_name = 'professor/criar_turma.html'

    def form_valid(self, form):
        turma = form.save(commit=False)
        turma.professor = self.request.user
        turma.save()
        return redirect('professor_home')