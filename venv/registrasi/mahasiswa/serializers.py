import imp
from rest_framework import serializers
from .models import Mahasiswa,OrangTua
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class MahasiswaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ('__all__')

class OrangTuaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrangTua
        fields = ('__all__')