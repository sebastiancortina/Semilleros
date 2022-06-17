from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from rest_framework_simplejwt.views import TokenObtainPairView
from usuarios.views import  UserViewSet, UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'',UserViewSet, basename='cutareadel')

urlpatterns = [
    path(r'usuarios/list', include(router.urls)),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/', UserView.as_view()),
]