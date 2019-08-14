from django.contrib import admin
from django.urls import path, include

from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls'))
]