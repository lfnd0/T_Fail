from django.urls import path, include

from .views import professor

urlpatterns = [
    path('professor', professor.TurmaListView.as_view(), name='professor_home'),
    path('professor/adicionar', professor.TurmaCreateView.as_view(), name='adicionar_turma')
]