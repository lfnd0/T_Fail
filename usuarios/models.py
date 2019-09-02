from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    is_estudante = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username']

    def __str__(self):
        return self.username

class Estudante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.username

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.username