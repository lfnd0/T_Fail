from django.urls import include, path

from .views import estudantes, professores, usuarios

urlpatterns = [
    path('', usuarios.home, name='home'),

    path('professores/', include(([
        path('', professores.TurmaListView.as_view(), name='listar_turmas'),
        path('turma/adicionar/', professores.TurmaCreateView.as_view(), name='adicionar_turma'),
        path('turma/<int:pk>/', professores.TurmaUpdateView.as_view(), name='atualizar_turma'),
        path('turma/<int:pk>/adicionar/matricula/', professores.adicionar_estudante, name='adicionar_estudante'),
    ], 'usuario'), namespace='professores'))
]