from tarfile import NUL
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    jewelrytypes = (('Necklace', 'Necklace'), ('Bracelet', 'Bracelet'), ('Ring', 'Ring'), ('Earring', 'Earring'), ('Anklet', 'Anklet'), ('Hairclip', 'Hairclip'), )
    colortypes = (('Black', 'Black'), ('Gold', 'Gold'), ('Copper', 'Copper'), ('Silver', 'Silver'), ('Brown', 'Brown'),)
    price = models.FloatField()
    jewelrytype = models.CharField(max_length=50, choices=jewelrytypes, default='necklace')
    description = models.TextField(blank=True, max_length=300)
    color = models.CharField(max_length=50, choices=colortypes, default='Black')
    code = models.TextField(max_length=10)
    image = models.ImageField(upload_to='images/')

    def _str_(self):
        return self.code

class Customer(models.Model):
    user = models.OneToOneField(User, null = True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
    def _str_(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    
    def _str_(self):
        return self.id

class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.address





