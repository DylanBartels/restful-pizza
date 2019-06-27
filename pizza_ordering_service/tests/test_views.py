import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Pizza
from ..serializers import PizzaSerializer

client = Client()

class GetAllPizzasTest(TestCase):
    """ Test module for GET all pizzas API """

    def setUp(self):
        Pizza.objects.create(flavor='margherita', size='small')
        Pizza.objects.create(flavor='margherita', size='medium')
        Pizza.objects.create(flavor='pepperoni', size='large')
        Pizza.objects.create(flavor='pepperoni', size='small')

    def test_get_all_pizzas(self):
        # get API response
        response = client.get(reverse('PizzaList'))
        # get data from db
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
