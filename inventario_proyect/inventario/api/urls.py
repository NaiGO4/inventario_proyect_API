from rest_framework.routers import DefaultRouter
from inventario.api.view import ProductoViewSet

router = DefaultRouter()
router.register('productos', ProductoViewSet, basename = 'producto')
urlpatterns = router.urls
