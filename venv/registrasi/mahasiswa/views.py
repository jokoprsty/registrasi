from rest_framework import viewsets
from .models import User, Mahasiswa, OrangTua
from .serializers import UserSerializer,MahasiswaSerializer, OrangTuaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MahasiswaView(viewsets.ModelViewSet):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

class OrangTua(viewsets.ModelViewSet):
    queryset = OrangTua.objects.all()
    serializer_class = OrangTuaSerializer