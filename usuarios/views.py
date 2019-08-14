from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .models import User
from .forms import EstudanteSignUpForm, ProfessorSignUpForm

def home(request):
    return render(request, 'home.html')

class SignUpView(TemplateView):
    template_name = 'signup.html'

class EstudanteSignUpView(CreateView):
    model = User
    form_class = EstudanteSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'estudante'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class ProfessorSignUpView(CreateView):
    model = User
    form_class = ProfessorSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'professor'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')