from rest_framework import serializers
from pizza_ordering_service.models import Pizza, Order


## PrimaryKeyRelatedField
class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    pizzas = serializers.PrimaryKeyRelatedField(many=True, queryset=Pizza.objects.all())

    class Meta:
        model = Order
        fields = '__all__'
