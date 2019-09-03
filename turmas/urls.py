from django.urls import include, path

from .views import estudantes, professores, usuarios

urlpatterns = [
    path('', usuarios.home, name='home'),

    path('professores/', include(([
        path('', professores.TurmaListView.as_view(), name='listar_turmas'),
        path('turma/adicionar/', professores.TurmaCreateView.as_view(), name='adicionar_turma')
    ], 'usuario'), namespace='professores'))
]