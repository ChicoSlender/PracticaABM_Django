from django.db import models
from django.db.models.fields import AutoField, CharField, DecimalField, IntegerField
from django.urls import reverse

# Create your models here.

class Empleado(models.Model):
    # Campos
    legajo = AutoField(primary_key=True)
    nombre = CharField(max_length=100)
    apellido = CharField(max_length=100)
    salario = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['legajo']
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' - ' + str(self.legajo)

    def get_absolute_url(self):
        return reverse('detalle-empleado', kwargs={'pk': self.legajo})