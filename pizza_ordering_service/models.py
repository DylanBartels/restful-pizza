from django.db import models
from django.core.validators import MinValueValidator


STATUS_CHOICES = (
	('created', 'Created'),
	('paid', 'Paid'),
	('preparing', 'Preparing'),
	('delivering', 'Delivering'),
    ('delivered', 'Delivered')
)
PIZZA_FLAVORS = [(x, x) for x in ['margherita', 'pepperoni', 'mozzarella']]
PIZZA_SIZES = [(x, x) for x in ['small', 'medium', 'large']]


class Pizza(models.Model):
    flavor = models.CharField(choices=PIZZA_FLAVORS, max_length=50)
    size   = models.CharField(choices=PIZZA_SIZES, max_length=50)
    amount = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    price  = models.DecimalField(decimal_places=2, max_digits=5, default=0.00)

    def __str__(self):
        return f'{self.amount} {self.size} pizza {self.flavor}'


class User(models.Model):
    customer_name    = models.CharField(max_length=100, default='')
    created          = models.DateTimeField(auto_now_add=True)
    customer_address = models.CharField(max_length=100, default='')
    customer_city    = models.CharField(max_length=100, default='')
    zip_code         = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.customer_name}'


class Order(models.Model):
    created  = models.DateTimeField(auto_now_add=True)
    status   = models.CharField(choices=STATUS_CHOICES, default='ordered', max_length=50)
    payment  = models.BooleanField(default=False)
    subtotal = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    pizzas   = models.ManyToManyField(Pizza)
    user     = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'id: {self.id}'

    # def update_subtotal(self):
	# 	subtotal = 0
	# 	for pizza in self.pizzas.all():
	# 		subtotal += pizza.price
	# 	self.subtotal = "%.2f" %(subtotal)
    #     self.save()
