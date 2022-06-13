from django.db import models
from django.contrib.auth.models import User
from apps.semilleros.models import Semillero


# Create your models here.
class Perfil(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usuario")
    id_semillero = models.ForeignKey(Semillero, on_delete=models.CASCADE, related_name="perfil")
    rol = models.CharField(max_length=250, default='estudiante', null=True)
    ni = models.BigIntegerField('Numero de identificacion')
    fecha_n = models.CharField('FECHA DE NACIMIENTO', max_length=250)
    direccion = models.CharField('DIRECCIÓN RESIDENCIA', max_length=250)
    l_espedicion = models.CharField('LUGAR DE EXPEDICIÓN ID', max_length=250)
    l_nacimiento = models.CharField('LUGAR DE NACIMIENTO', max_length=250)
    telefono = models.BigIntegerField('TELÉFONO/ CELULAR')
    n_emergencia = models.CharField('EN CASO DE EMERGENCIA LLAMAR A', max_length=250)
    numero_emergencia = models.CharField('NÚMERO DE CONTACTO', max_length=250) 
    programa = models.CharField('Programa', max_length=250, null=True, blank=True)
    año_i = models.CharField('AÑO INGRESO', max_length=250,  null=True, blank=True)
    semestre_a = models.CharField('SEMESTRE ACTUAL', max_length=250,  null=True, blank=True)
    f_grado =  models.CharField('FECHA DE GRADO', max_length=250,  null=True, blank=True)
    pregrado = models.CharField('PREGRADO', max_length=250, null=True, blank=True)
    posgrado = models.CharField('POSGRADOS', max_length=250, null=True, blank=True)
    
    def __str__(self):
        return str(self.username)

    
