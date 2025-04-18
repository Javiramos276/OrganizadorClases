from django.db import models
from Usuarios.models import Alumno,Docente

# Create your models here.
class Clase(models.Model):
    docente_a_cargo = models.ForeignKey(Docente, on_delete= models.CASCADE) # Un docente puede tener muchos docentes a cargo
    fecha_dictado = models.DateField()
    horario_inicio = models.TimeField()
    horario_finalizacion = models.TimeField()
    precio = models.DecimalField(max_digits=10)
    lista_alumnos = models.ManyToManyField(Alumno)

    def __str__(self):
        return f"Clase de {self.docente_a_cargo} en {self.fecha_dictado} para {self.lista_alumnos}"
    
    def modificar_horario_clase(self):
        """
        Modifica el horario de inicio de una clase
        """
        pass

    def modificar_dia_clase(self):
        """
        Modifica el dia de una clase
        """
        pass

    def quitar_alumno_clase(self,alumno):
        """
        Elimina a un alumno de la lista de alumnos de la clase
        """
        pass

    def agregar_alumno_a_clase(self,alumno):
        """
        Agrega un alumno a una clase
        """
        pass

class Materia(models.Model):
    nivel = [
        ("PRI", 'Primario'),
        ("SEC", 'Secundario'),
        ("TER", 'Terciario'),
        ("UNI", 'Universitario'),
    ]
    nivel_educativo = models.CharField(max_length=3, choices=nivel)
    nombre_materia = models.CharField(max_length=100)
    precio_por_hora = models.DecimalField(max_digits=10)
    
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Alumno, on_delete=models.CASCADE)  # Un estudiante se inscribe en una clase
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)  # La inscripción está asociada a una clase

    def __str__(self):
        return f"{self.estudiante} inscrito en {self.clase}"
