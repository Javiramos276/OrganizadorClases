from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, blank=True)
    telefono = models.CharField(max_length=20, unique=True, blank=True, null=True)

class Docente(Usuario):
    materias = [
        ("AL", 'Algebra Lineal'),
        ("AM1", 'Analisis matematico 1'),
        ("AM2", 'Analisis matematico 2'),
    ]
    materias_dictadas = models.CharField(max_length=3, choices=materias)

    def agregar_clase(Alumno,Clase):
        """
        Alumno (Objeto)
        Clase (Objeto)
        Crea una instancia de la clase
        """
        pass

    def eliminar_clase(Alumno,Clase):
        """
        Alumno (Objeto)
        Clase (Objeto)
        Elimina una instancia de la clase
        """
        pass


class Alumno(Usuario):

    def proximas_clases():
        """
        Retorna las proximas clases que tiene un alumno
        """
        pass