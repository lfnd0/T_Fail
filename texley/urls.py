from django.contrib import admin
from django.urls import path, include

from usuarios import views
from turmas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('turmas', include('turmas.urls'))
]