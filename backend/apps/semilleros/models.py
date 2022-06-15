from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Semillero(models.Model):
    #id_users = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    #id_users = models.ManyToManyField(User, related_name="perfil")
    nombre = models.CharField('NOMBRE DEL SEMILLERO', max_length=250)
    facultad = models.CharField('FACULTAD', max_length=250)
    programa_academico = models.CharField('PROGRMA ACADÉMICO', max_length=250)
    g_investigacion = models.CharField('GRUPO DE INVESTIGACIÓN AL CUAL ESTÁ VINCULADO EL SEMILLERO',max_length=250)
    l_investigacion_asociado = models.CharField('LÍNEA Y SUBLÍNEA DE INVESTIGACIÓN ASOCIADOS', max_length=250)
    tematica = models.CharField('TÉMATICA DE ESTUDIO DEL SEMILLERO', max_length=250)
    justificacion = models.TextField(' JUSTIFICACIÓN DEL SEMILLERO DE INVESTIGACIÓN')
    status = models.BooleanField('Aprobacion', default=False)
    activo = models.BooleanField('Activo', default=False)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre   
