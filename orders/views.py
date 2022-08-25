from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order, OrderItem
from cart.cart import Cart
from .tasks import process_payment


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # Create new order
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

        serializer = OrderSerializer(order)
        result = serializer.data.copy()
        result['total_cost'] = int(order.get_total_cost())
        result['message'] = "Sucess, order created"
        process_payment.delay(order.id)
        cart.clear()
        return Response(result, status=status.HTTP_201_CREATED)
