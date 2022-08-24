from .serializers import OrderSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Order
import ipdb
from cart.cart import Cart
from rest_framework import status
from rest_framework.response import Response
from .models import OrderItem

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
    
"""
    def create(self, request):
        cart = Cart(request=request)
        if len(cart) == 0:
            return Response({'message': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        if cart.get_total_quantity() == 0:
            return Response({'message': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
"""