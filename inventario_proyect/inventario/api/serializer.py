from rest_framework import serializers
from inventario.models import Producto

class ProductoSerializer(serializers.ModelSerilizer):
    class Meta:
        model = Producto
        fields = '__all__'