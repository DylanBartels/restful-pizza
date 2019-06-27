from django.test import TestCase
from ..models import Pizza


class PizzaTest(TestCase):
    """ Test module for Pizza model """

    def setUp(self):
        Pizza.objects.create(flavor='margherita', size='small')
        Pizza.objects.create(flavor='pepperoni', size='medium')
        Pizza.objects.create(flavor='mozzarella', size='large')

    def test_pizza(self):
        pizza_small_margherita = Pizza.objects.get(flavor='margherita')
        pizza_medium_pepperoni = Pizza.objects.get(flavor='pepperoni')
        pizza_large_mozzarella = Pizza.objects.get(flavor='mozzarella')

        self.assertEqual(pizza_small_margherita.get_pizza(), '1 small pizza margherita')
        self.assertEqual(pizza_medium_pepperoni.get_pizza(), '1 medium pizza pepperoni')
        self.assertEqual(pizza_large_mozzarella.get_pizza(), '1 large pizza mozzarella')
