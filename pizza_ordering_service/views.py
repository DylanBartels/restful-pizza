from rest_framework.viewsets import ModelViewSet
from pizza_ordering_service.serializers import UserSerializer, OrderSerializer, PizzaSerializer
from pizza_ordering_service.models import User, Order, Pizza


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class PizzaViewSet(ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
