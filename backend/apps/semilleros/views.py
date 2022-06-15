
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from api.serializers import SemilleroSerializer, UsuarioSerializer, PerfilSerializer
from apps.semilleros.models import Semillero
from django.contrib.auth.models import User
from apps.usuarios.models import Perfil

# Create your views here.

class SemillerolistAV(APIView):
    
    # Listar semilleros
    def get(self, request):
        semilleros = Semillero.objects.filter(activo=True)
        serializer = SemilleroSerializer(semilleros, many=True)
        user = self.request.user.id
    
        return Response(serializer.data)
    
    

    #Crear semillero
    def post(self, request):
        serializer = SemilleroSerializer(data=request.data)
        #serializer2 =PerfilSerializer(data=request.data["perfil"])
        #print( serializer2)
        #serializer = SemilleroSerializer(data=request.data)

        if serializer.is_valid():
            Perfil.objects.all()
            #if 
            #usuarios = serializer.data['perfil']
            
            #serializer.save()
            
            
            
            
            
            
            return Response(serializer.data['id'], status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
