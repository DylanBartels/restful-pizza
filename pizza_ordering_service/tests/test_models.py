from django.test import TestCase
from ..models import Pizza, Order, Customer, Specification
from .helpers import get_dummy_order


class PizzaTest(TestCase):
    """ Test module for Pizza model """

    def setUp(self):
        get_dummy_order()

    def test_pizza(self):
        pizza_small_mozzarella = Specification.objects.get(size='small')
        pizza_medium_margherita = Specification.objects.get(size='medium')
        pizza_large_pepperoni = Specification.objects.get(size='large')

        self.assertEqual(str(pizza_small_mozzarella), '3 small pizza mozzarella')
        self.assertEqual(str(pizza_medium_margherita), '30 medium pizza margherita')
        self.assertEqual(str(pizza_large_pepperoni), '7 large pizza pepperoni')

class OrderTest(TestCase):
    """ Test module for Order model """

    def setUp(self):
        get_dummy_order()

    def test_order(self):
        order = Order.objects.get(status='creating')
        self.assertEqual(str(order), 'creating order containing: 3 pizzas')
