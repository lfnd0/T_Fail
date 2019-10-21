from django.contrib import admin

from .models import User, Estudante, Professor, Turma, Atividade, Problema, Submissao

admin.site.register(User)
admin.site.register(Estudante)
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Problema)
admin.site.register(Atividade)
admin.site.register(Submissao)