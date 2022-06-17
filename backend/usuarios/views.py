from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password

from .models import User
from api.serializers import UsuarioSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    
    permission_classes = [IsAdminUser]
    serializer_class = UsuarioSerializer
    queryset = User.objects.all()

    #     request.data['password'] = make_password(request.data['password'])
    #     return super().create(request.data, *args, **kwargs)




    # def partial_update(self, request, *args, **kwargs):
    #     password = request.data['password']
    #     if password:
    #         request.data['password'] = make_password(password)
    #     else:
    #         request.data['password'] = request.user.password

    #     return super().update(request, *args, **kwargs)
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer =  UsuarioSerializer(request.user)
        return Response(serializer.data)
