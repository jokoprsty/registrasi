
from django.db import models
from django.contrib.auth.models import User

class Mahasiswa(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class OrangTua(models.Model):
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
# Create your models here.
