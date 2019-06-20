from django.urls import include, path

from .views import classroom

urlpatterns = [
    path('', classroom.home, name='home'),
]