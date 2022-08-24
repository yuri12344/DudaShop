import json
from .serializers import OrderSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Order
import ipdb
from cart.cart import Cart
from rest_framework import status
from rest_framework.response import Response
from .models import OrderItem
from django.http import HttpResponse
from django.http import JsonResponse


"""
 - Receive the order via JSON
 - Create a new order by the data entered and instantiate and associate each OrderItem with item in the cart
 - Clear all cart content and return success message
"""

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # TODO
    # Get the cart from the session, and iterate over then to catch the products and create an OrderItem for each product.
    
    # - Remove product id
    # - Return the products in the order
    def create(self, request):
        cart = Cart(request)
        if len(cart) == 0:
            return Response({"message": "your cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        if cart.get_total_quantity() == 0:
            return Response({"message": "your cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(**serializer.data)

        for item in cart:
            price = int(item['product'].price)
            quantity = item['quantity']
            OrderItem.objects.create(order=order, product=item['product'], price=price, quantity=quantity)

        # cart.clear()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

"""
    def create(self, request):
        cart = Cart(request=request)
        if len(cart) == 0:
            return Response({'message': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        if cart.get_total_quantity() == 0:
            return Response({'message': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
"""