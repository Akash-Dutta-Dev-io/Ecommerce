from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Buyer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    company_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product_images/')
    price = models.CharField(max_length=10, default=0)
    description = models.TextField()

    def __str__(self):
        return self.product_name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s Cart Item - {self.product.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')  
    alt_phone = models.CharField(max_length=100, default='')  
    state = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    house_no = models.CharField(max_length=100, default='')
    area = models.CharField(max_length=100, default='')
    nearby = models.CharField(max_length=100, default='')
    address = models.TextField()
    CHOICES = [('Home', 'Home'), ('Office', 'Office')]
    option_choice = models.CharField(max_length=20, choices=CHOICES, default='')

    def __str__(self):
        return f"Order #{self.pk} - {self.user.username} - {self.product.title}"