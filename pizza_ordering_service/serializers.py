from rest_framework import serializers
from pizza_ordering_service.models import Pizza, Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    pizzas = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='pizza-detail'
    )

    class Meta:
        model = Order
        fields = '__all__'


class PizzaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pizza
        fields = '__all__'
