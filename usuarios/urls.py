from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/signup/', views.SignUpView.as_view(), name='signup'),
    path('usuarios/signup/estudante/', views.EstudanteSignUpView.as_view(), name='estudante_signup'),
    path('usuarios/signup/professor/', views.ProfessorSignUpView.as_view(), name='professor_signup')
]