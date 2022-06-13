from django.shortcuts import render
from django.urls import path, include

#from apps.semilleros.views import SemillerolistAV, SemilleroDetalleAV, SemillerolistAprobado
from apps.semilleros.views import *
from apps.usuarios.views import *

# Create your views here.
urlpatterns = [
    path('list',  SemillerolistAV.as_view(), name='semillero-list'),
    path('usuarios/list',  UserlistAV.as_view(), name='usuarios-list'),
    path('usuarios/perfil',   UserperfillistAV.as_view(), name='usuarios-perfil'),

   # path('<int:id>', SemilleroDetalleAV.as_view(), name='semillero-detalle'),
   # path('aprobados', SemillerolistAprobado.as_view(), name='semillero-aprobado'),

   # path('usuarios/list',  UsuariolistAV.as_view(), name=' usuario-list'),
   # path('usuarios/<int:id>',  UsuarioDetalleAV.as_view(), name=' usuario-detalle')
]
