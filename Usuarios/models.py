from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from Clases.models import Materia

# Create your models here.

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, blank=True)
    telefono = models.CharField(max_length=20, unique=True, blank=True, null=True)

class Docente(Usuario):
    materias_dictadas = models.ManyToManyField(Materia)

    def agregar_clase(self,Alumno):
        """
        Alumno (Objeto)
        Clase (Objeto)
        Crea una instancia de la clase
        """
        pass

    def eliminar_clase(self,Alumno):
        """
        Alumno (Objeto)
        Clase (Objeto)
        Elimina una instancia de la clase
        """
        pass

    def mostrar_clases_del_dia(self):
        """
        Retorna todas las clases que tiene el profesor en el dia
        """
        pass

class Alumno(Usuario):

    def proximas_clases():
        """
        Retorna las proximas clases que tiene un alumno
        """
        pass