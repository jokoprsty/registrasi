from rest_framework import routers
from .views import UserView, MahasiswaView

router = routers.SimpleRouter()
router.register(r'users', UserView)
router.register(r'mahasiswa',MahasiswaView)
urlpatterns = router.urls
