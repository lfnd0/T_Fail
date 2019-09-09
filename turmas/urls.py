from django.urls import include, path

from .views import estudantes, professores, usuarios

urlpatterns = [
    path('', usuarios.home, name='home'),

    path('estudantes/', include(([
        path('', estudantes.TurmaListView.as_view(), name='listar_turmas_estudante')
    ], 'usuario'), namespace='estudantes')),

    path('professores/', include(([
        path('', professores.TurmaListView.as_view(), name='listar_turmas'),
        path('turma/adicionar/', professores.TurmaCreateView.as_view(), name='adicionar_turma'),
        path('turma/<int:pk>/', professores.TurmaUpdateView.as_view(), name='atualizar_turma')
    ], 'usuario'), namespace='professores'))
]