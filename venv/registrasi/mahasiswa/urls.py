from rest_framework import routers
from .views import MahasiswaView

router = routers.DefaultRouter()
router.register(r'mahasiswa',MahasiswaView)