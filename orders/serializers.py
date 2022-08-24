from rest_framework import serializers
from .models import Order, OrderItem
import ipdb

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'product',
            'price',
            'quantity'
            )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'items')

