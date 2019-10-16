from django.db import models

# Create your models here.
class Usuario(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Email =models.EmailField()
    FechaNac =models.DateField()

class Administrador(models.Model):
    id = models.IntegerField( primary_key=True)
    Nombre =models.CharField(max_length=50)
    Apellido =models.CharField(max_length=50)

class Chef(models.Model):
    Rut =models.CharField(max_length=12, primary_key=True)
    Nombre =models.CharField(max_length=50)
    Apellido =models.CharField(max_length=50)
