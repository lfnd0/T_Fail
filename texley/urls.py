from django.contrib import admin
from django.urls import path, include

from app.views import usuarios, estudantes, professores

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app.urls')),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/signup/', usuarios.SignUpView.as_view(), name='signup'),
    path('usuarios/signup/estudante/', estudantes.EstudanteSignUpView.as_view(), name='estudante_signup'),
    path('usuarios/signup/professor/', professores.ProfessorSignUpView.as_view(), name='professor_signup')
]