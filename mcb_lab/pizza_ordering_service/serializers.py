from rest_framework import serializers
from pizza_ordering_service.models import Pizza, Order


class OrderSerializer(serializers.ModelSerializer):
    pizzas = serializers.PrimaryKeyRelatedField(many=True, queryset=Pizza.objects.all())

    class Meta:
        model = Order
        fields = ('id', 'status', 'pizzas')


class PizzaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pizza
        fields = ('id', 'flavor', 'size', 'amount')
