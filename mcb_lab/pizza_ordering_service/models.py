from django.db import models

STATUS_CHOICES = ['ordered', 'preparing', 'delivering', 'delivered']
PIZZA_FLAVORS = ['margherita', 'pepperoni', 'mozzarella']
PIZZA_SIZES = ['small', 'medium', 'large']

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default='ordered', max_length=100)

    class Meta:
        ordering = ('created',)

class Pizza(models.Model):
    flavor = models.MultipleChoiceField(required=True, choices=PIZZA_FLAVORS)
    size = models.MultipleChoiceField(required=True, choices=PIZZA_SIZES)
    amount = models.IntegerField(required=True, default=1)

    class Meta:
        ordering = ('created',)
