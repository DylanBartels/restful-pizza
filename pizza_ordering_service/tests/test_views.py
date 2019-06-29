import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Pizza, Order
from ..serializers import PizzaSerializer

client = Client()

class GetAllPizzasTest(TestCase):
    """ Test module for GET all pizzas API """

    def setUp(self):
        Order.objects.create(status='creating')
        Pizza.objects.create(flavor='margherita', size='small', order=Order.objects.get(status='creating'))
        Pizza.objects.create(flavor='margherita', size='medium', order=Order.objects.get(status='creating'))
        Pizza.objects.create(flavor='pepperoni', size='large', order=Order.objects.get(status='creating'))
        Pizza.objects.create(flavor='pepperoni', size='small', order=Order.objects.get(status='creating'))

    def test_get_all_pizzas(self):
        # get API response
        response = client.get(reverse('pizza-list'))
        # get data from db
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSinglePizzaTest(TestCase):
    """ Test module for GET single pizza API """

    def setUp(self):
        Order.objects.create(status='creating')
        Pizza.objects.create(flavor='margherita', size='small', order=Order.objects.get(status='creating'))
        Pizza.objects.create(flavor='margherita', size='medium', order=Order.objects.get(status='creating'))
        Pizza.objects.create(flavor='pepperoni', size='small', order=Order.objects.get(status='creating'))
        self.large_pepperoni = Pizza.objects.create(flavor='pepperoni', size='large', order=Order.objects.get(status='creating'))

    def test_get_valid_single_pizza(self):
        response = client.get(
            reverse('pizza-detail', kwargs={'pk': self.large_pepperoni.pk}))
        pizza = Pizza.objects.get(pk=self.large_pepperoni.pk)
        serializer = PizzaSerializer(pizza)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_pizza(self):
        response = client.get(
            reverse('pizza-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
