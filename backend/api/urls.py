from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import  UserViewSet 



router_user = DefaultRouter()


router_user.register(
    prefix='users', basename='users', viewset=UserViewSet
)


# urlpatterns = [
#      path('users/list', UserViewSet.as_view(), name='list-user'),
#     # path('api/v1/semillero/', include("usuarios.urls")),
    
# ]
