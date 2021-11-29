from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UsuariosSr(models.Model):
    cod_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30, blank=True, null=True)
    pais = models.CharField(max_length=30, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuarios_sr'


class Calificaciones(models.Model):
    cod_calificacion = models.AutoField(primary_key=True)
    cod_usuario = models.IntegerField(blank=True, null=True)
    cod_videojuego = models.IntegerField(blank=True, null=True)
    puntuacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calificaciones'
