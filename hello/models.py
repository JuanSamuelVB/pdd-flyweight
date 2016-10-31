from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class SaborDeNieve(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

    def __unicode__(self):
        return self.nombre + ' ' + self.apellido

class Orden(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    sabor = models.ForeignKey('SaborDeNieve', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
