from rest_framework import DefaultRouter
from inventario.api.serializer import ProductoViewSet

router = DefaultRouter()
router.register('productos', ProductoViewSet, basename = 'producto')
urlpatterns = router.urls
