from rest_framework import routers
from .views import MahasiswaView

router = routers.SimpleRouter()
router.register(r'mahasiswa',MahasiswaView)
urlpatterns = router.urls