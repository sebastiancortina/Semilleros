
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from api.serializers import SemilleroSerializer, UsuarioSerializer
from apps.semilleros.models import Semillero
from django.contrib.auth.models import User

# Create your views here.

class SemillerolistAV(APIView):
    
    # Listar semilleros
    def get(self, request):
        semilleros = Semillero.objects.filter(activo=True)
        serializer = SemilleroSerializer(semilleros, many=True)
        return Response(serializer.data)
    

    #Crear semillero
    def post(self, request):
        serializer = SemilleroSerializer(data=request.data)

        #serializer = SemilleroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
