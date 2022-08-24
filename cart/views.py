from django.shortcuts import get_object_or_404
from .cart import Cart
from store.models import Product
from .serializers import CartAddOrUpdateProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CartView(APIView):
    def get(self, request):
        """Get cart"""
        cart = Cart(request)
        return Response(cart.__dict__['cart'], status=status.HTTP_200_OK)


    def post(self, request, product_id):
        """Add product to cart or update his quantity"""
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        serializer = CartAddOrUpdateProductSerializer(data=request.data)
        
        if serializer.is_valid():
            cart.add(product=product, quantity=serializer.data['quantity'])

        return Response(cart.__dict__['cart'], status=status.HTTP_200_OK)


    def put(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        serializer = CartAddOrUpdateProductSerializer(data=request.data)

        if serializer.is_valid():
            cart.update(product=product, quantity=serializer.data['quantity'])

        return Response(cart.__dict__['cart'], status=status.HTTP_200_OK)



    def delete(self, request, product_id):
        """Delete a product from cart"""

        cart = Cart(request) # check if exists or create a new
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return Response(cart.__dict__['cart'], status=status.HTTP_200_OK)

    



        