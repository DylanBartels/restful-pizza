from rest_framework.viewsets import ModelViewSet
from pizza_ordering_service.serializers import UserSerializer, OrderSerializer, PizzaSerializer
from pizza_ordering_service.models import User, Order, Pizza


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = (
        Order.objects
            .select_related(
                'user',
            )
            .prefetch_related(
                'pizzas',
            )
        )

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)

        # For debugging purposes only.
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        for query in connection.queries:
            print(query['sql'])
        return response


class PizzaViewSet(ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
