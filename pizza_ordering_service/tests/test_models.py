from django.test import TestCase
from ..models import Pizza, Order


class PizzaTest(TestCase):
    """ Test module for Pizza model """

    def setUp(self):
        Order.objects.create(status='creating')
        Pizza.objects.create(flavor='margherita', size='small', order=Order.objects.get(status='creating'))
        Pizza.objects.create(flavor='pepperoni', size='medium', order=Order.objects.get(status='creating'))
        Pizza.objects.create(flavor='mozzarella', size='large', order=Order.objects.get(status='creating'))

    def test_pizza(self):
        pizza_small_margherita = Pizza.objects.get(flavor='margherita')
        pizza_medium_pepperoni = Pizza.objects.get(flavor='pepperoni')
        pizza_large_mozzarella = Pizza.objects.get(flavor='mozzarella')

        self.assertEqual(str(pizza_small_margherita), '1 small pizza margherita')
        self.assertEqual(str(pizza_medium_pepperoni), '1 medium pizza pepperoni')
        self.assertEqual(str(pizza_large_mozzarella), '1 large pizza mozzarella')

class OrderTest(TestCase):
    """ Test module for Order model """

    def setUp(self):
        Order.objects.create(status='creating')
        Pizza.objects.create(flavor='margherita', size='small', order=Order.objects.get(status='creating'))
        Pizza.objects.create(flavor='pepperoni', size='medium', order=Order.objects.get(status='creating'))
        Pizza.objects.create(flavor='mozzarella', size='large', order=Order.objects.get(status='creating'))

    def test_order(self):
        order = Order.objects.get(status='creating')
        self.assertEqual(str(order), 'creating order containing: 3 pizzas')
