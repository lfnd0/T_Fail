from django.urls import path, include

from . import views

urlpatterns = [
    path('professor', views.TurmaListView.as_view(), name='professor_home'),
    path('professor/adicionar', views.TurmaCreateView.as_view(), name='criar_turma')
]