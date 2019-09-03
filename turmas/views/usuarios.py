from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_professor:
            return redirect('professores:listar_turmas')
        else:
            return render(request, 'usuario/home.html')
    return render(request, 'usuario/home.html')