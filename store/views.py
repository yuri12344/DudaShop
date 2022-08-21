from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from rest_framework import viewsets


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
