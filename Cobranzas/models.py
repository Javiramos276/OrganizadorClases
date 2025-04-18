from django.db import models

class MetodoPago(models.TextChoices):
    EFECTIVO = 'EF', 'Efectivo'
    TARJETA = 'TR', 'Tarjeta'
    TRANSFERENCIA = 'TT', 'Transferencia'

class Pago(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(
        max_length=2,
        choices=MetodoPago.choices, 
        default=MetodoPago.TRANSFERENCIA,
    )

    estado_pago = [
        ("PAGA", 'Pagado'),
        ("PEND", 'Pendiente'),
    ]
    estado = models.TextField(max_length=4, choices= estado_pago)
    
    def __str__(self):
        return f"Pedido con método de pago: {self.metodo_pago}"

    def confirmar_pago(self):
        """
        Dado un alumno y una clase, confirma el pago de la case
        """
        pass

    def cancelar_pago(self):
        """
        Dado un alumno y una clase, cancela el pago si se cancelo la clase.
        """
        pass

    def calcular_pago(self,docente,tiempo):
        """
        Dado un docente, calcula el pago por el tiempo trabajado.

        Args:
        docente (Docente): Instancia del docente para el cual se calcula el pago.
        tiempo (str): Intervalo de tiempo. Opciones válidas: "dia", "semana", "quincena", "mes".
        """
        pass
