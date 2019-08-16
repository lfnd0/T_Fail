from django.db import models

from usuarios.models import Professor

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Turmas'
    
    def __str__(self):
        return self.nome