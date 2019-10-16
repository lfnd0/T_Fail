from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    is_estudante = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Estudante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.username

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.username

class Turma(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='turmas')
    estudantes = models.ManyToManyField(Estudante, blank=True)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Submissao(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    codigo = models.FileField(upload_to='respostas/codigo')
    raw_loc = models.DecimalField(max_digits=5, decimal_places=2)
    raw_lloc = models.DecimalField(max_digits=5, decimal_places=2)
    raw_sloc = models.DecimalField(max_digits=5, decimal_places=2)
    hal_total_h1 = models.DecimalField(max_digits=5, decimal_places=2)
    hal_total_h2 = models.DecimalField(max_digits=5, decimal_places=2)
    hal_total_N1 = models.DecimalField(max_digits=5, decimal_places=2)
    hal_total_N2 = models.DecimalField(max_digits=5, decimal_places=2)
    hal_total_vocabulary = models.DecimalField(max_digits=5, decimal_places=2)
    hal_total_length = models.DecimalField(max_digits=5, decimal_places=2)
    hal_total_volume = models.DecimalField(max_digits=5, decimal_places=2)
    hal_total_difficulty = models.DecimalField(max_digits=5, decimal_places=2)
    hal_total_effort = models.DecimalField(max_digits=5, decimal_places=2)
    hal_total_time = models.DecimalField(max_digits=5, decimal_places=2)
    hal_total_bugs = models.DecimalField(max_digits=5, decimal_places=2)