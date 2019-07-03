from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from pizza_ordering_service.serializers import CustomerSerializer, OrderSerializer, PizzaSerializer
from pizza_ordering_service.models import Customer, Order, Pizza


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = (
        Order.objects
            .select_related('customer')
            .prefetch_related('pizzas')
        )
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status', 'customer__name',)

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)

        # # For debugging purposes only.
        # from django.db import connection
        # print('# of Queries: {}'.format(len(connection.queries)))
        # for query in connection.queries:
        #     print(query['sql'])
        
        return response


class PizzaViewSet(ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
