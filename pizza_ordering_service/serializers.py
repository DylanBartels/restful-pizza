from rest_framework import serializers
from pizza_ordering_service.models import Pizza, Order, User
from drf_writable_nested import WritableNestedModelSerializer


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'


class OrderSerializer(WritableNestedModelSerializer):
    pizzas = PizzaSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    subtotal = serializers.IntegerField(read_only=True)
    payment = serializers.BooleanField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
