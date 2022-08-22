from unicodedata import category
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    @action(detail=True, methods=['GET'])
    def products(self, request, pk=None):
        category = self.get_object()
        serializer = CategorySerializer(category.products.all(), many=True)
        return Response(serializer.data)


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

