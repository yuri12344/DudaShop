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

        expected_return = [{
         	"id": 14,
         	"first_name": "Yuri",
         	"last_name": "Caetano",
         	"email": "yuuri.caetano@gmail.com",
         	"address": "Rua Henriqe",
         	"postal_code": "83060460",
         	"city": "Sao Jose dos pinhais",
            "product_details": []
            }]

        res = []


        for item in cart:
            order_item = {
                "order": "1",
                "product": item['product'].name,
                "price": int(item['price']),
                "quantity": item['quantity']
            }
            res.append(order_item)
            # OrderItem.objects.create(order=self.order, product=item['product'], price=item['price'], quantity=item['quantity'])
        expected_return[0]['product_details'] = res
        cart.clear()

        return HttpResponse(json.dumps(expected_return), status=status.HTTP_201_CREATED)

"""
    def create(self, request):
        cart = Cart(request=request)
        if len(cart) == 0:
            return Response({'message': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        if cart.get_total_quantity() == 0:
            return Response({'message': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
"""