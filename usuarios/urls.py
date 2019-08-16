from django.urls import include, path
from . import views
from turmas.views import listar_turmas, criar_nova_turma

urlpatterns = [
    path('', views.home, name='home'),
    path('contas/', include('django.contrib.auth.urls')),
    path('contas/signup/', views.SignUpView.as_view(), name='signup'),
    path('contas/signup/estudante', views.EstudanteSignUpView.as_view(), name='estudante_signup'),
    path('contas/signup/professor', views.ProfessorSignUpView.as_view(), name='professor_signup'),
    path('contas/professor/turmas', listar_turmas, name='listagem_turmas'),
    path('contas/professor/criar', criar_nova_turma, name='nova_turma')
]