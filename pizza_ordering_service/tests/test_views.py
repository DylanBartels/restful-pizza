import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Pizza, Order, Specification, Customer
from ..serializers import OrderSerializer
from .helpers import get_dummy_order

client = Client()

class GetAllOrdersTest(TestCase):
    """ Test module for GET all orders API """

    def setUp(self):
        get_dummy_order()

    def test_get_all_orders(self):
        # get API response
        response = client.get(reverse('order-list'))
        # get data from db
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleOrderTest(TestCase):
    """ Test module for GET single order API """

    def setUp(self):
        self.order = get_dummy_order()

    def test_get_valid_single_order(self):
        response = client.get(
            reverse('order-detail', kwargs={'pk': self.order.pk}))
        order_item = Order.objects.get(pk=self.order.pk)
        serializer = OrderSerializer(order_item)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_order(self):
        response = client.get(
            reverse('order-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewOrderTest(TestCase):
    """ Test module for inserting a new order """

    def setUp(self):
        get_dummy_order()
        self.valid_payload = {
            "customer": {
                "name": "Dylan Bartels",
                "address": "Kantstrasse 86",
                "city": "Berlin",
                "zip_code": "781644"
            },
            "pizzas": [
              {
                "flavor": "margherita",
                "size": "small",
                "quantity": 10
              },
              {
                "flavor": "pepperoni",
                "size": "large",
                "quantity": 4
              }
            ],
            "payment": True,
            "status": "created"
        }

        self.invalid_payload = {
            'flavor': 'pepperoni',
            'size': 'large',
            'order': 'delivered'
        }

    def test_create_valid_order(self):
        response = client.post(
            reverse('order-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_order(self):
        response = client.post(
            reverse('order-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
