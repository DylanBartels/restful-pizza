from django.db import models
from django.core.validators import MinValueValidator


STATUS_CHOICES = (
	('created', 'Created'),
	('paid', 'Paid'),
	('preparing', 'Preparing'),
	('delivering', 'Delivering'),
    ('delivered', 'Delivered')
)
PIZZA_FLAVORS = (
    ('margherita', 'Margherita'),
    ('pepperoni', 'Pepperoni'),
    ('mozzarella', 'Mozzarella')
)
PIZZA_SIZES = (
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large')
)


class Pizza(models.Model):
    flavor     = models.CharField(choices=PIZZA_FLAVORS, max_length=50, unique=True)

    def __str__(self):
        return f'{self.flavor}'


class Customer(models.Model):
    name     = models.CharField(max_length=100, default='')
    created  = models.DateTimeField(auto_now_add=True)
    address  = models.CharField(max_length=100, default='')
    city     = models.CharField(max_length=100, default='')
    zip_code = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    created  = models.DateTimeField(auto_now_add=True)
    status   = models.CharField(choices=STATUS_CHOICES, default='ordered', max_length=50)
    payment  = models.BooleanField(default=False)
    pizzas   = models.ManyToManyField(Pizza, through='Specification', related_name='orders')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'id: {self.id}'


class Specification(models.Model):
    pizza    = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order    = models.ForeignKey(Order, on_delete=models.CASCADE)
    size     = models.CharField(choices=PIZZA_SIZES, max_length=50, default='medium')
    quantity = models.IntegerField(validators=[MinValueValidator(1)], default=1)
