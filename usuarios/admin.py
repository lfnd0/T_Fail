from django.contrib import admin

from .models import User, Estudante, Professor

admin.site.register(User)
admin.site.register(Estudante)
admin.site.register(Professor)