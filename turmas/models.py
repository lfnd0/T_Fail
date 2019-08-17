from django.db import models

from usuarios.models import User

class Turma(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='turmas')
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome