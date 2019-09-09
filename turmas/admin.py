from django.contrib import admin

from .models import User, Estudante, Professor, Turma

admin.site.register(User)
admin.site.register(Estudante)
admin.site.register(Professor)
admin.site.register(Turma)