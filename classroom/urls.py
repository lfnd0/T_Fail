from django.urls import path

from .views import classroom

urlpatterns = [
    path('', classroom.home, name='home'),
]