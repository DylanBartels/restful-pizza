from rest_framework import serializers
from pizza_ordering_service.models import Pizza, Order, User


## PrimaryKeyRelatedField
class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    # ordered_pizzas = PizzaSerializer(many=True)
    # pizzas = serializers.PrimaryKeyRelatedField(many=True, queryset=Pizza.objects.all())

    class Meta:
        model = Order
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        fields = '__all__'
