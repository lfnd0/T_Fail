from django.urls import include, path

from .views import estudantes, professores, usuarios

urlpatterns = [
    path('', usuarios.home, name='home'),
    path('turmas/',usuarios.turma, name='turma'),

    path('estudantes/', include(([
        path('', estudantes.TurmaListView.as_view(), name='listar_turmas_estudante'),
        path('turma/adicionar/submissao', estudantes.SubmissaoCreateView.as_view(), name='adicionar_submissao')
    ], 'usuario'), namespace='estudantes')),

    path('professores/', include(([
        path('', professores.TurmaListView.as_view(), name='listar_turmas_professor'),
        path('turma/adicionar/', professores.TurmaCreateView.as_view(), name='adicionar_turma'),
        path('turma/<int:pk>/adicionar/estudante/', professores.TurmaUpdateView.as_view(), name='atualizar_turma'),
        path('turma/<int:pk>/adicionar/atividade/', professores.adicionar_atividade, name='adicionar_atividade'),
        path('turma/<int:id>/deletar/', professores.deletar_turma, name='deletar_turma')
    ], 'usuario'), namespace='professores'))
]