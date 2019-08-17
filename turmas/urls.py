from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.TurmaListView.as_view(), name='professor_home'),
    path('professor/nova', views.TurmaCreateView.as_view(), name='criar_turma')
]