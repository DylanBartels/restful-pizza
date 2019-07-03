from rest_framework import serializers
from pizza_ordering_service.models import Pizza, Order, Customer, Specification
from pizza_ordering_service.validators import is_list, is_dict

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
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        customer_data = validated_data.pop("customer")
        customer = Customer.objects.create(**customer_data)
        order = Order.objects.create(customer=customer, **validated_data)

        if "pizzas" in self.initial_data:
            if is_list(self.initial_data.get("pizzas"), "pizzas"):
                pizzas = self.initial_data.get("pizzas")

                for pizza in pizzas:
                    if is_dict(pizza, "pizza"):
                        pizza_data = SpecificationSerializer(data=pizza)
                        if pizza_data.is_valid():
                            size = pizza.get("size")
                            quantity = pizza.get("quantity")
                            pizza_instance = Pizza.objects.get(flavor=pizza.get("flavor"))
                            Specification(order=order, pizza=pizza_instance, size=size, quantity=quantity).save()

        order.save()
        return order

    def update(self, instance, validated_data):
        if instance.status != "delivered":
            if "pizzas" in self.initial_data:
                if is_list(self.initial_data.get("pizzas"), "pizzas"):
                    pizzas = self.initial_data.get("pizzas")
                    order = Order.objects.get(id=instance.id)
                    old_specs = Specification.objects.filter(order=order)
                    old_specs.delete()

                    for pizza in pizzas:
                        if is_dict(pizza, "pizza"):
                            pizza_data = SpecificationSerializer(data=pizza)
                            if pizza_data.is_valid():
                                size = pizza.get("size")
                                quantity = pizza.get("quantity")
                                pizza_instance = Pizza.objects.get(flavor=pizza.get("flavor"))
                                Specification(order=order, pizza=pizza_instance, size=size, quantity=quantity).save()

            instance.status = validated_data["status"]
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("Delivered orders cannot be changed")
