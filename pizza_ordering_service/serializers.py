from rest_framework import serializers
from pizza_ordering_service.models import Pizza, Order, Customer, Specification


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='pizza.id')
    flavor = serializers.ReadOnlyField(source='pizza.flavor')
    price = serializers.ReadOnlyField(source='pizza.price')

    class Meta:
        model = Specification
        fields = ('id', 'flavor', 'size', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    pizzas = SpecificationSerializer(source="specification_set", many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        customer = Customer.objects.create(
            zip_code = self.initial_data["customer"]["zip_code"],
            city = self.initial_data["customer"]["city"],
            name = self.initial_data["customer"]["name"],
            address = self.initial_data["customer"]["address"]
        )
        order = Order.objects.create(customer=customer, **validated_data)
        if "pizzas" in self.initial_data:
            pizzas = self.initial_data.get("pizzas")
            for pizza in pizzas:
                size = pizza.get("size")
                flavor = pizza.get("flavor")
                quantity = pizza.get("quantity")
                pizza_instance = Pizza.objects.get(flavor=flavor)
                Specification(order=order, pizza=pizza_instance, size=size, quantity=quantity).save()
        order.save()
        return order

    def update(self, instance, validated_data):
        Specification.objects.filter(Order=instance).delete()
        pizzas = self.initial_data.get("pizzas")
        for pizza in pizzas:
            size = pizza.get("size")
            flavor = pizza.get("flavor")
            quantity = pizza.get("quantity")
            pizza_instance = Pizza.objects.get(flavor=flavor)
            Specification(order=order, pizza=pizza_instance, size=size, quantity=quantity).save()

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance
