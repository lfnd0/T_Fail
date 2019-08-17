from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contas/', include('django.contrib.auth.urls')),
    path('contas/signup/', views.SignUpView.as_view(), name='signup'),
    path('contas/signup/estudante/', views.EstudanteSignUpView.as_view(), name='estudante_signup'),
    path('contas/signup/professor/', views.ProfessorSignUpView.as_view(), name='professor_signup'),
    
]