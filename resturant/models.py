from django.db import models

# Create your models here.
# authentication/models.py

from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    # Add more custom fields as needed

    # def __str__(self):
    #     return self.username


class Categorys(models.Model):
    category_name = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.category_name

class Products(models.Model):
    category_name = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    offer = models.IntegerField(default=0)
    size = models.CharField(max_length=30)
    stock = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    on_discount = models.BooleanField(default=False)
    discount_price = models.FloatField(blank=True, null=True)    
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

# orders/models.py

# from django.db import models

# class FoodItem(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=8, decimal_places=2)

class Order(models.Model):
    product_name = models.ForeignKey(Products, on_delete=models.CASCADE)#, through='OrderItem'
    category_name = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product_name = models.ForeignKey(Products, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()


#test purpose
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username