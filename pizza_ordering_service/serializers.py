from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from pizza_ordering_service.models import Pizza, Order, User


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class OrderSerializer(WritableNestedModelSerializer):
    user     = UserSerializer()
    pizzas   = PizzaSerializer(many=True)
    subtotal = serializers.IntegerField(read_only=True)
    payment  = serializers.BooleanField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        depth = 1
