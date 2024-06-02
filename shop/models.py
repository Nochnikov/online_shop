from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} : {self.description}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} : {self.description}'

class Order(models.Model):
    status_choice = (
        ('Pending', 'Pending'),
        ('processed', 'Processed'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
        ('shipped', 'Shipped'),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=status_choice, default='Pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    order_item = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.user} : {self.status} {self.total_price}'
