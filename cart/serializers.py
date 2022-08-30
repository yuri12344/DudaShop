from rest_framework import serializers


class CartAddOrUpdateProductSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)
