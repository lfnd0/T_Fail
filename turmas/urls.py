from django.urls import include, path

from .views import estudantes, professores, usuarios

urlpatterns = [
    path('', usuarios.home, name='home'),
    path('turmas/',usuarios.turma, name='turma'),

    path('estudantes/', include(([
        path('', estudantes.TurmaListView.as_view(), name='listar_turmas_estudante'),
        path('turma/<int:pk>/listar/atividades/', estudantes.listar_atividades, name='listar_atividades_estudante'),
        path('turma/atividade/<int:pk>/listar/problemas/', estudantes.listar_problemas, name='listar_problemas_estudante'),
        path('turma/atividade/problema/<int:pk>/adicionar/submissao/', estudantes.adicionar_submissao, name='adicionar_submissao'),
        path('turma/atividade/problema/<int:pk>/listar/submissoes', estudantes.listar_submissoes, name='listar_submissoes_estudante')
    ], 'usuario'), namespace='estudantes')),

    path('professores/', include(([
        path('', professores.TurmaListView.as_view(), name='listar_turmas_professor'),
        path('turma/adicionar/', professores.TurmaCreateView.as_view(), name='adicionar_turma'),
        path('turma/<int:id>/deletar/', professores.deletar_turma, name='deletar_turma'),
        path('turma/<int:pk>/adicionar/estudante/', professores.TurmaUpdateView.as_view(), name='atualizar_turma'),
        path('turma/<int:pk>/listar/atividades', professores.listar_atividades, name='listar_atividades_professor'),
        path('turma/<int:pk>/adicionar/atividade/', professores.adicionar_atividade, name='adicionar_atividade'),
        path('turma/atividade/<int:id>/deletar/', professores.deletar_atividade, name='deletar_atividade'),
        path('turma/atividade/<int:pk>/listar/problemas/', professores.listar_problemas, name='listar_problemas_professor'),
        path('turma/atividade/<int:pk>/adicionar/problema/', professores.adicionar_problema, name='adicionar_problema'),
        path('turma/atividade/problema/<int:id>/deletar/', professores.deletar_problema, name='deletar_problema'),
        path('turma/atividade/problema/<int:pk>/listar/submissoes/', professores.listar_submissoes, name='listar_submissoes_professor'),
        path('turma/atividade/problema/submissao/<int:pk>/adicionar/avaliacao', professores.adicionar_avaliacao, name='adicionar_avaliacao')
    ], 'usuario'), namespace='professores'))
]