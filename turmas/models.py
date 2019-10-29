from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
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
    instituto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Atividade(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='atividades')
    titulo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titulo
    
class Problema(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='problemas')
    pergunta = models.CharField(max_length=200)
    def __str__(self):
        return self.pergunta

class Submissao(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    problema = models.ForeignKey(Problema, on_delete=models.CASCADE, related_name='submissoes')
    codigo = models.FileField(upload_to='submissoes')
    raw_loc = models.IntegerField()
    raw_lloc = models.IntegerField()
    raw_sloc = models.IntegerField()
    hal_total_h1 = models.IntegerField()
    hal_total_h2 = models.IntegerField()
    hal_total_N1 = models.IntegerField()
    hal_total_N2 = models.IntegerField()
    hal_total_vocabulary = models.IntegerField()
    hal_total_length = models.IntegerField()
    hal_total_calculated_length = models.DecimalField(max_digits=8, decimal_places=2)
    hal_total_volume = models.DecimalField(max_digits=8, decimal_places=2)
    hal_total_difficulty = models.DecimalField(max_digits=8, decimal_places=2)
    hal_total_effort = models.DecimalField(max_digits=8, decimal_places=2)
    hal_total_time = models.DecimalField(max_digits=8, decimal_places=4)
    hal_total_bugs = models.DecimalField(max_digits=8, decimal_places=4)