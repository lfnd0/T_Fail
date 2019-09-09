from django.contrib import admin

from .models import User, Estudante, Professor, Turma, Matricula

admin.site.register(User)
admin.site.register(Estudante)
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Matricula)