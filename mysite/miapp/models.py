from django.db import models

def generar_factores(desde=8, hasta=38):
    return {
        f'factor{i}': models.DecimalField(max_digits=10, decimal_places=8, default=0)
        for i in range(desde, hasta + 1)
    }

class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    instrumento = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    fecha_pago = models.DateField(null=True, blank=True)
    valor_historico = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    # inyecta factor8 ... factor38
    locals().update(generar_factores())

    class Meta:
        db_table = 'CALIFICACION'

    def __str__(self):
        return f"{self.instrumento} - {self.descripcion}"