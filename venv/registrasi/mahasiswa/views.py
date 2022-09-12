import imp
from rest_framework import viewsets
from .models import Mahasiswa, OrangTua
from .serializers import MahasiswaSerializer, OrangTuaSerializer
# Create your views here.


class MahasiswaView(viewsets.ModelViewSet):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

class OrangTua(viewsets.ModelViewSet):
    queryset = OrangTua.objects.all()
    serializer_class = OrangTuaSerializer