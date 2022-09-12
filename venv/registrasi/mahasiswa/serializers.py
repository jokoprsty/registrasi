import imp
from rest_framework import serializers
from .models import Mahasiswa,OrangTua

class MahasiswaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ('__all__')

class OrangTuaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrangTua
        fields = ('__all__')