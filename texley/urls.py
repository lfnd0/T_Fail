from django.contrib import admin
from django.urls import path, include

from usuarios import views
from turmas import views

urlpatterns = [
    path('', include('usuarios.urls')),
    path('admin/', admin.site.urls),
    path('turmas/', include('turmas.urls'))
]