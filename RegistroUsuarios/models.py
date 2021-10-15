from django.db import models
from django import forms

#Modelo para el tipo de documento
class tipodocumento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

#Modelo para Ciudad
class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

#Modelo para Persona
class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    idtipodocumento = models.ForeignKey(tipodocumento, on_delete=models.CASCADE)
    documento = models.IntegerField()
    idlugarresiedencia = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fechadenacimiento = models.DateField()
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=15)
    confirmarcontraseña = models.CharField(max_length=15)
    lugardenacimiento = models.CharField(max_length=50)