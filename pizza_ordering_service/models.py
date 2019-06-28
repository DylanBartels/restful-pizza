from django.db import models

STATUS_CHOICES = [(x, x) for x in ['creating', 'ordered', 'preparing', 'delivering', 'delivered']]
PIZZA_FLAVORS = [(x, x) for x in ['margherita', 'pepperoni', 'mozzarella']]
PIZZA_SIZES = [(x, x) for x in ['small', 'medium', 'large']]

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default='ordered', max_length=50)

    class Meta:
        ordering = ('created',)

class Pizza(models.Model):
    order = models.ForeignKey(Order, related_name='pizzas', on_delete=models.CASCADE)
    flavor = models.CharField(choices=PIZZA_FLAVORS, max_length=50)
    size = models.CharField(choices=PIZZA_SIZES, max_length=50)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.amount} {self.size} pizza {self.flavor}'
