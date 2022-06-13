from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UsuarioSerializer, PerfilSerializer
from apps.usuarios.models import Perfil


# Create your views here.
class UserlistAV(APIView):
    
    # Listar user
    def get(self, request):
        semilleros = User.objects.all()
        serializer = UsuarioSerializer(semilleros, many=True)
        return Response(serializer.data)
    
    
    #Crear semillero
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        
        #serializer = SemilleroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserperfillistAV(APIView):
    
    # Listar user
    def get(self, request):
        semilleros = Perfil.objects.all()
        serializer = PerfilSerializer(semilleros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerfilSerializer(data=request.data)
        
        #serializer = SemilleroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

