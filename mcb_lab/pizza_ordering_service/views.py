from pizza_ordering_service.models import Order, Pizza
from pizza_ordering_service.serializers import OrderSerializer, PizzaSerializer
from rest_framework import generics


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PizzaList(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetail(generics.RetrieveAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
