from rest_framework import serializers
from inventario.models import Producto
from inventario.api.serializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializers_class = ProductoSerializer