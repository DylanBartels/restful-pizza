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
        self.large_pepperoni = Pizza.objects.create(
            flavor='pepperoni', size='large', order=Order.objects.get(status='creating'))

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

class CreateNewPizzaTest(TestCase):
    """ Test module for inserting a new pizza """

    def setUp(self):
        Order.objects.create(status='creating')
        self.valid_payload = {
            'flavor': 'margherita',
            'size': 'small',
            'order': Order.objects.get(status='creating')
        }
        self.invalid_payload = {
            'flavor': 'pepperoni',
            'size': 'large',
            'order': ''
        }

    def test_create_valid_pizza(self):
        response = client.post(
            reverse('pizza-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_pizza(self):
        response = client.post(
            reverse('pizza-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSinglePizzaTest(TestCase):
    """ Test module for deleting an existing pizza record """

    def setUp(self):
        Order.objects.create(status='creating')
        self.large_pepperoni = Pizza.objects.create(
            flavor='pepperoni', size='large', order=Order.objects.get(status='creating'))
        self.medium_mozzarella = Pizza.objects.create(
            flavor='mozzarella', size='medium', order=Order.objects.get(status='creating'))

    def test_valid_delete_pizza(self):
        response = client.delete(
            reverse('pizza-detail', kwargs={'pk': self.large_pepperoni.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_pizza(self):
        response = client.delete(
            reverse('pizza-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
